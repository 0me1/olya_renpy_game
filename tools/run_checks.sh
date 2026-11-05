#!/bin/bash
set -euo pipefail
cd "$(dirname "$0")/.."
: "${RENPY_SDK:?Set RENPY_SDK to your RenPy 8 SDK directory}"
python3 tests/check_project.py
"$RENPY_SDK/renpy.sh" "$PWD" lint
"$RENPY_SDK/renpy.sh" "$PWD" test routes
"$RENPY_SDK/renpy.sh" "$PWD" test interface --overwrite-screenshots
"$RENPY_SDK/renpy.sh" "$PWD" test layout
"$RENPY_SDK/renpy.sh" "$PWD" test integration --overwrite-screenshots
"$RENPY_SDK/renpy.sh" "$PWD" test framing --overwrite-screenshots
