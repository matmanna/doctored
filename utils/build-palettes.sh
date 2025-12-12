#!/usr/bin/env bash
set -euo pipefail

ROOT_DIR="$(cd "$(dirname "$0")/.." && pwd)"
INPUT="$ROOT_DIR/assets/css/tailwind.css"
OUTDIR="$ROOT_DIR/_includes/palettes"
CSSOUT="$ROOT_DIR/assets/css"

PALETTES=(
  slate gray zinc neutral stone red orange amber yellow lime green emerald teal cyan sky
  blue indigo violet purple fuchsia pink rose
)

mkdir -p "$OUTDIR"
mkdir -p "$CSSOUT"

if [ ! -f "$INPUT" ]; then
  echo "Input CSS not found: $INPUT" >&2
  exit 1
fi

echo "Building Tailwind palette variants into:"
echo "  CSS:  $CSSOUT"
echo "  HTML: $OUTDIR"

for p in "${PALETTES[@]}"; do
  echo "-> Building palette: $p"

  CSS_FILE="$CSSOUT/main.$p.css"
  HTML_FILE="$OUTDIR/main.$p.html"

  PRIMARY_PALETTE=$p npx tailwindcss -i "$INPUT" -o "$CSS_FILE" --minify

  {
    echo "<style>"
    sed -E 's#/assets/([^)"]+)#{{ "/assets/\1" | relative_url }}#g' "$CSS_FILE"
    echo "</style>"
  } > "$HTML_FILE"
done

echo "Done."
