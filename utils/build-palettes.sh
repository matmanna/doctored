#!/usr/bin/env bash
set -euo pipefail

ROOT_DIR="$(cd "$(dirname "$0")/.." && pwd)"
INPUT="$ROOT_DIR/assets/css/tailwind.css"
OUTDIR="$ROOT_DIR/assets/css"

PALETTES=(
  slate gray zinc neutral stone red orange amber yellow lime green emerald teal cyan sky
  blue indigo violet purple fuchsia pink rose
)

if [ ! -f "$INPUT" ]; then
  echo "Input CSS not found: $INPUT" >&2
  exit 1
fi

echo "Building Tailwind palette variants into $OUTDIR"

for p in "${PALETTES[@]}"; do
  echo "-> Building palette: $p"
  PRIMARY_PALETTE=$p npx tailwindcss -i "$INPUT" -o "$OUTDIR/main.$p.css" --minify
done

echo "Done."
