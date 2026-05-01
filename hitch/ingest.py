from __future__ import annotations

import csv
import hashlib
import io
from dataclasses import dataclass
from pathlib import Path
from typing import Iterable

from .paths import DEFAULT_RAW_CSV, INGEST_DIR
from .storage import now_iso, write_json, write_jsonl


MESSAGE_PATH = INGEST_DIR / "girlfriend_messages.jsonl"
SOURCE_META_PATH = INGEST_DIR / "source_meta.json"


@dataclass(frozen=True)
class MessageRecord:
    message_id: str
    timestamp: str | None
    sender: str
    text: str


def detect_encoding(path: Path) -> str:
    sample = path.read_bytes()[:8192]
    if sample.startswith((b"\xff\xfe", b"\xfe\xff")) or sample.count(b"\x00") > 0:
        return "utf-16"
    for encoding in ("utf-8-sig", "cp949", "euc-kr"):
        try:
            sample.decode(encoding)
            return encoding
        except UnicodeDecodeError:
            continue
    return "utf-8-sig"


def read_text(path: Path) -> tuple[str, str]:
    encoding = detect_encoding(path)
    return path.read_text(encoding=encoding, errors="replace"), encoding


def _candidate(headers: Iterable[str], names: set[str]) -> str | None:
    for header in headers:
        normalized = header.strip().lower()
        if normalized in names:
            return header
    for header in headers:
        normalized = header.strip().lower()
        if any(name in normalized for name in names):
            return header
    return None


def _message_id(index: int, timestamp: str | None, sender: str, text: str) -> str:
    digest = hashlib.sha256(f"{index}|{timestamp}|{sender}|{text}".encode("utf-8")).hexdigest()
    return digest[:16]


def _parse_dict_rows(rows: list[dict[str, str]]) -> list[MessageRecord]:
    if not rows:
        return []
    headers = list(rows[0])
    timestamp_key = _candidate(headers, {"date", "datetime", "timestamp", "time", "날짜", "일시"})
    sender_key = _candidate(headers, {"sender", "user", "name", "author", "speaker", "작성자", "보낸사람"})
    text_key = _candidate(headers, {"message", "text", "content", "body", "내용", "메시지"})
    records: list[MessageRecord] = []
    for index, row in enumerate(rows, start=1):
        values = {key: (value or "").strip() for key, value in row.items()}
        timestamp = values.get(timestamp_key, "") if timestamp_key else ""
        sender = values.get(sender_key, "") if sender_key else ""
        text = values.get(text_key, "") if text_key else ""
        if not text:
            ignored = {timestamp_key, sender_key}
            candidates = [value for key, value in values.items() if key not in ignored and value]
            text = max(candidates, key=len) if candidates else ""
        if not sender:
            sender = "unknown"
        if text:
            records.append(MessageRecord(_message_id(index, timestamp or None, sender, text), timestamp or None, sender, text))
    return records


def _parse_list_rows(rows: list[list[str]]) -> list[MessageRecord]:
    records: list[MessageRecord] = []
    for index, row in enumerate(rows, start=1):
        cells = [cell.strip() for cell in row if cell and cell.strip()]
        if not cells:
            continue
        if len(cells) >= 3:
            timestamp, sender = cells[0], cells[1]
            text = " ".join(cells[2:])
        elif len(cells) == 2:
            timestamp, sender, text = None, "unknown", cells[1]
        else:
            timestamp, sender, text = None, "unknown", cells[0]
        records.append(MessageRecord(_message_id(index, timestamp, sender, text), timestamp, sender, text))
    return records


def parse_csv(path: Path = DEFAULT_RAW_CSV) -> tuple[list[MessageRecord], dict[str, object]]:
    text, encoding = read_text(path)
    sample = text[:8192]
    try:
        dialect = csv.Sniffer().sniff(sample)
    except csv.Error:
        dialect = csv.excel
    has_header = False
    try:
        has_header = csv.Sniffer().has_header(sample)
    except csv.Error:
        pass

    if has_header:
        reader = csv.DictReader(io.StringIO(text), dialect=dialect)
        records = _parse_dict_rows(list(reader))
    else:
        reader = csv.reader(io.StringIO(text), dialect=dialect)
        records = _parse_list_rows(list(reader))

    meta = {
        "source": str(path),
        "encoding": encoding,
        "bytes": path.stat().st_size,
        "parsed_records": len(records),
        "ingested_at": now_iso(),
    }
    return records, meta


def ingest_girlfriend_csv(path: Path = DEFAULT_RAW_CSV) -> dict[str, object]:
    if not path.exists():
        raise FileNotFoundError(f"Missing required local input: {path}")
    records, meta = parse_csv(path)
    write_jsonl(MESSAGE_PATH, (record.__dict__ for record in records))
    write_json(SOURCE_META_PATH, meta)
    return meta
