#!/bin/bash
set -euo pipefail
cd "$(dirname "$0")"

echo "loop.sh is the local executable simulation/demo loop contract for Hitch."
echo "It is intended to run prepare -> simulation -> demo style rehearsal steps once the local runnable code path exists."
echo "The actual runnable implementation stays local and may be regenerated before rehearsal."
