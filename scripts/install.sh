#!/usr/bin/env bash
set -euo pipefail

ROOT_DIR="$(cd "$(dirname "${BASH_SOURCE[0]}")/.." && pwd)"
DEST_DIR="${CODEX_HOME:-$HOME/.codex}/skills/medical-photo-reader"

mkdir -p "$(dirname "$DEST_DIR")"
rm -rf "$DEST_DIR"
cp -R "$ROOT_DIR/skills/medical-photo-reader" "$DEST_DIR"

echo "Installed medical-photo-reader skill to: $DEST_DIR"
