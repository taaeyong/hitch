"""Relationship-space domain model and persistence."""

from __future__ import annotations

import re
from dataclasses import dataclass, field
from pathlib import Path
from typing import Any

from .storage import read_json, utc_now_iso, write_json


VALID_LOVE_LANGUAGE_MODES = {"simple", "deep"}


class RelationshipSpaceError(ValueError):
    pass


def slugify(value: str) -> str:
    normalized = re.sub(r"[^a-zA-Z0-9가-힣_-]+", "-", value.strip()).strip("-")
    return normalized.lower() or "relationship"


@dataclass(frozen=True)
class RelationshipSpace:
    space_id: str
    relationship_type: str
    partner_label: str
    current_state: str
    daily_delivery_time: str
    love_language_mode: str
    created_at: str
    updated_at: str
    owner_ref: str = "local-user"
    metadata: dict[str, Any] = field(default_factory=dict)

    @classmethod
    def create(
        cls,
        *,
        relationship_type: str,
        partner_label: str,
        current_state: str,
        daily_delivery_time: str,
        love_language_mode: str,
        owner_ref: str = "local-user",
        space_id: str | None = None,
    ) -> "RelationshipSpace":
        validate_creation_set(
            relationship_type=relationship_type,
            partner_label=partner_label,
            current_state=current_state,
            daily_delivery_time=daily_delivery_time,
            love_language_mode=love_language_mode,
        )
        now = utc_now_iso()
        resolved_space_id = space_id or f"{slugify(relationship_type)}-{slugify(partner_label)}"
        return cls(
            space_id=resolved_space_id,
            relationship_type=relationship_type.strip(),
            partner_label=partner_label.strip(),
            current_state=current_state.strip(),
            daily_delivery_time=daily_delivery_time.strip(),
            love_language_mode=love_language_mode.strip(),
            created_at=now,
            updated_at=now,
            owner_ref=owner_ref,
        )

    @classmethod
    def from_dict(cls, payload: dict[str, Any]) -> "RelationshipSpace":
        return cls(**payload)

    def to_summary(self) -> dict[str, str]:
        return {
            "space_id": self.space_id,
            "relationship_type": self.relationship_type,
            "partner_label": self.partner_label,
            "current_state": self.current_state,
            "daily_delivery_time": self.daily_delivery_time,
            "love_language_mode": self.love_language_mode,
        }


def validate_creation_set(
    *,
    relationship_type: str,
    partner_label: str,
    current_state: str,
    daily_delivery_time: str,
    love_language_mode: str,
) -> None:
    required = {
        "relationship_type": relationship_type,
        "partner_label": partner_label,
        "current_state": current_state,
        "daily_delivery_time": daily_delivery_time,
        "love_language_mode": love_language_mode,
    }
    missing = [name for name, value in required.items() if not str(value).strip()]
    if missing:
        raise RelationshipSpaceError(f"Missing relationship-space fields: {', '.join(missing)}")
    if love_language_mode not in VALID_LOVE_LANGUAGE_MODES:
        raise RelationshipSpaceError(
            "love_language_mode must be one of: "
            + ", ".join(sorted(VALID_LOVE_LANGUAGE_MODES))
        )
    if not re.fullmatch(r"[0-2][0-9]:[0-5][0-9]", daily_delivery_time.strip()):
        raise RelationshipSpaceError("daily_delivery_time must use HH:MM format")


def space_dir(data_dir: Path, space_id: str) -> Path:
    return data_dir / "relationships" / slugify(space_id)


def metadata_path(data_dir: Path, space_id: str) -> Path:
    return space_dir(data_dir, space_id) / "metadata.json"


def save_space(data_dir: Path, space: RelationshipSpace) -> Path:
    return write_json(metadata_path(data_dir, space.space_id), space)


def load_space(data_dir: Path, space_id: str) -> RelationshipSpace:
    payload = read_json(metadata_path(data_dir, space_id), default=None)
    if payload is None:
        raise FileNotFoundError(f"No relationship space found for {space_id}")
    return RelationshipSpace.from_dict(payload)


def get_or_create_demo_space(data_dir: Path, space_id: str = "demo-relationship") -> RelationshipSpace:
    path = metadata_path(data_dir, space_id)
    if path.exists():
        return load_space(data_dir, space_id)
    space = RelationshipSpace.create(
        space_id=space_id,
        relationship_type="romantic_partner",
        partner_label="상대",
        current_state="서로를 더 잘 이해하고 싶은 관계",
        daily_delivery_time="21:30",
        love_language_mode="deep",
    )
    save_space(data_dir, space)
    return space
