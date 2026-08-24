#!/usr/bin/env bash
# GORIPOLY - budowanie plikow do drukarni.
# Renderuje karty.html w headless Chrome i zapisuje PDF-y w tym katalogu.
# Wszystkie strony 62 x 93 mm = netto 56 x 87 + spad 3 mm z kazdej strony.
set -euo pipefail

CHROME="/Applications/Google Chrome.app/Contents/MacOS/Google Chrome"
ROOT="$(cd "$(dirname "$0")/.." && pwd)"
OUT="$ROOT/druk"
SRC="file://$ROOT/karty.html"

pdf () { # pdf <plik> <query>
  local name="$1"; shift
  echo "-> $name"
  "$CHROME" --headless=new --disable-gpu --no-pdf-header-footer \
    --virtual-time-budget=20000 --run-all-compositor-stages-before-draw \
    --print-to-pdf="$OUT/$name" "$SRC?$1" 2>/dev/null
}

pdf "GORIPOLY-fronty-wzory.pdf"   "tryb=single&filtr=fronty&marks=0"
pdf "GORIPOLY-fronty-naklad.pdf"  "tryb=single&filtr=fronty&naklad=1&marks=0"
pdf "GORIPOLY-rewers.pdf"         "tryb=single&filtr=back&marks=0"
pdf "GORIPOLY-proof-A4.pdf"       "naklad=1&marks=1"

echo
python3 "$OUT/kontrola.py" "$OUT"/GORIPOLY-*.pdf
