#!/usr/bin/env python3
"""Kontrola plikow do drukarni: format strony, liczba stron, osadzone fonty.
Uzycie: python3 kontrola.py plik.pdf [plik2.pdf ...]"""
import re, sys, os

MM = 25.4/72
OCZEK = (62.0, 93.0)   # element karty ze spadem


def info(path):
    d = open(path, 'rb').read()
    pages = len(re.findall(rb'/Type\s*/Page[^s]', d))
    boxes = set()
    for m in re.findall(rb'/MediaBox\s*\[([^\]]*)\]', d):
        v = [float(x) for x in m.split()]
        boxes.add((round((v[2]-v[0])*MM, 2), round((v[3]-v[1])*MM, 2)))
    fonts = sorted({f.decode().split('+')[-1] for f in
                    re.findall(rb'/BaseFont\s*/([A-Za-z0-9+\-,_]+)', d)})
    return pages, boxes, fonts, len(d)


for p in sys.argv[1:]:
    pages, boxes, fonts, size = info(p)
    name = os.path.basename(p)
    print(f"\n{name}  ({size/1_048_576:.1f} MB)")
    print(f"  stron: {pages}")
    for b in sorted(boxes):
        ok = "OK" if abs(b[0]-OCZEK[0]) < .3 and abs(b[1]-OCZEK[1]) < .3 else \
             ("A4 - to arkusz proof" if abs(b[0]-210) < 1 else "!! zly format")
        print(f"  strona: {b[0]} x {b[1]} mm  [{ok}]")
    poppins = [f for f in fonts if 'Poppins' in f]
    print(f"  fonty: {', '.join(fonts) if fonts else 'BRAK (same rastry)'}")
    if not poppins and fonts:
        print("  !! Poppins nie zaladowany - Chrome podstawil zapasowy font. "
              "Sprawdz internet i przebuduj, inaczej sklad w PDF-ie jest inny niz na ekranie.")
    print("  przestrzen: RGB (konwersja do CMYK po stronie drukarni albo w Acrobacie)")
