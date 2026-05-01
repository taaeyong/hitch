#!/bin/bash
set -euo pipefail
cd "$(dirname "$0")"

echo "run.sh is the local executable run contract for Hitch."
echo "It is intended to create or restore the runnable local rehearsal code path from the current docs/spec context."
echo "The actual runnable implementation stays local and may be regenerated before rehearsal."
