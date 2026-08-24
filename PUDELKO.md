# GORIpoly - pudełko na talię

Wymiary liczone z jednej wielkości, której nie da się wyczytać ze spec: **grubości jednej karty**.
Reszta wynika z formatu karty (56 x 87 mm netto, `files/SPEC-KART.md`) i liczby kart.

## 1. Liczba kart

| Grupa | Szt. |
|---|---|
| Talia podstawowa (z 3 kartami zasad) | 109 |
| Dodatek "karty przypału" | 8 |
| **Razem w pudełku** | **117** |

## 2. Grubość talii T

`T = 117 x t`, gdzie `t` to grubość jednej gotowej karty (z laminatem).

| Podłoże | t [mm] | T [mm] |
|---|---|---|
| 250 g bez laminatu (druk domowy) | 0,25 | 29,3 |
| 300 g karton do kart + laminat 2 str. (typowa drukarnia kart) | 0,31 | **36,3** |
| 310 g "blue core" (MPC S30/S33) | 0,32 | 37,4 |
| 350 g kreda + folia (drukarnia offsetowa / poligrafia lokalna) | 0,40 | 46,8 |

Jak zdjąć `t` bez zgadywania:
- **z próbki**: zmierz suwmiarką 20 wydrukowanych kart, podziel przez 20 (pojedyncza karta jest poza rozdzielczością pomiaru),
- **od drukarni**: w wycenie poproś o "grubość jednej karty po laminowaniu" albo o grubość talii 117 szt.,
- **od producenta talii**: MakePlayingCards / PrinterStudio podają caliper podłoża w specyfikacji stocku.

Domyślnie w tym dokumencie: `t = 0,31 mm`, `T = 36,3 mm`.

## 3. Wymiary pudełka

Luzy: **+1,5 mm** na szerokość i wysokość (karta ma wchodzić i wychodzić, nie ocierać o klapkę),
**+2 mm** na głębokość (talia po tasowaniu nie leży idealnie płasko).

| Wymiar | Wzór | Wartość dla T = 36,3 |
|---|---|---|
| Wewnętrzna szerokość | 56 + 1,5 | **57,5 mm** |
| Wewnętrzna wysokość | 87 + 1,5 | **88,5 mm** |
| Wewnętrzna głębokość | T + 2 | **38,5 mm** |
| Zewnętrzne (karton 0,4 mm) | wewnętrzne + 2 x 0,4 | 58,3 x 89,3 x 39,3 mm |

## 4. Rozkrój (tuck box, klapki wsuwane góra i dół)

| Element | Wymiar |
|---|---|
| Panel front / tył | 57,5 x 88,5 mm |
| Panel boczny (x2) | 38,5 x 88,5 mm |
| Panel zamykający góra / dół | 57,5 x 38,5 mm |
| Klapka wsuwana (góra i dół) | 14 mm |
| Skrzydełka pyłowe (dust flaps) | 36 mm (głębokość - 2,5 mm) |
| Klapka klejowa | 12 mm |
| **Rozkrój płasko** | ok. 204,5 x 193,5 mm |
| Ze spadem 3 mm | 210,5 x 199,5 mm |

Rozkrój mieści się na A4 poziomo, ale zostaje ok. 5 mm zapasu w pionie - drukuj bez marginesów
albo na A3/SRA3. Karton na pudełko: **350 g** (przy 117 kartach 300 g się rozłazi na bokach).

Generator rozkroju bez rysowania: <https://www.templatemaker.nl/en/cardbox/>, pola do wpisania:
`Length = 38,5` (głębokość), `Width = 57,5`, `Height = 88,5`, `Material Thickness = 0,4`,
`Tuck Flap Size = 14`, `Glue Flap Size = 12`, `Rounded Corners Radius = 3`, `Thumb Hole = 0`
(dziurka na palec psuje kompozycję frontu). Eksport: **SVG** - grafikę podkładasz pod rozkrój
w Illustratorze / Inkscape jako warstwę pod liniami cięcia i zgięć.

Jeśli talię drukuje drukarnia kart, **weź od nich rozkrój pudełka na 117 kart** i wsadź grafikę
w ich dieline. Wtedy nic nie liczysz - ich rozkrój uwzględnia ich karton i ich maszynę.

## 5. Prompt na grafikę pudełka

Model obrazkowy nie zrobi rozkroju - zrobi płaski panel. Dlatego prompt leci **osobno na każdy panel**,
a złożenie na rozkroju robisz w wektorach. Panel front to jedyny, który naprawdę wymaga generowania;
boki, tył i klapki składasz z tych samych elementów w Illustratorze.

Prompt trzyma się języka rewersu (`ILUSTRACJE.md`, sekcja 30), żeby pudełko i karty wyglądały jak jeden zestaw.

```
Create a luxurious, highly polished illustrated vector artwork for the FRONT PANEL of a board-game
box for a custom card game called "GORIPOLY".

IMPORTANT - CHARACTER IDENTITY:
Use the uploaded photos of my friend as the primary and authoritative reference for his identity.
Preserve his recognizable facial features, face shape, hairstyle, hair color, glasses, proportions
and overall appearance. Do not redesign, replace, beautify, age or significantly alter his face.
The character must clearly look like the same person from the reference photos. Only transform him
into a stylized illustrated/vector character. He is the game mascot and must match the character
already used on the card backs.

FORMAT - CRITICAL:
A flat, vertical rectangular panel in portrait orientation, proportions exactly 57,5 x 88,5 mm
(aspect ratio ~1:1.54). Straight, clean edges, no rounded corners, no perspective, no 3D box
mockup, no shadow under the box, no product photo. This is flat print artwork for a die-cut panel,
seen perfectly straight on. The artwork must bleed to all four edges with no white margin and no
frame gap at the edges. Do not draw the box itself, do not draw cards next to it, do not add
mockup lighting.

BACKGROUND:
Deep royal blue (#12294A) with a luxurious quilted diamond pattern and subtle geometric texture.
Rich, elegant, premium, slightly theatrical.

FRAME:
An intricate Art Deco metallic frame combining gold and silver elements: ornamental curves,
scrollwork, filigree, geometric Art Deco details, layered metallic highlights. The frame follows
the straight rectangular edges of the panel and sits 6 mm inside the panel edge, so nothing
important is lost when the panel is trimmed.

CHARACTER:
Upper center: an illustrated caricature portrait of my friend based directly on the uploaded photos,
wearing a black top hat, an elegant black tuxedo jacket, a gray bow tie and his characteristic
glasses. Confident, charismatic expression, slightly exaggerated cartoon proportions, clean vintage
vector illustration with crisp outlines and subtle dimensional shading. Place the portrait inside an
ornate silver metallic medallion with spiral scrollwork.

MAIN TITLE:
Directly below the medallion, a large centered red (#C8102E) banner with rounded corners, premium
dimensional appearance with subtle highlights and shadows, reading exactly:

GORIPOLY

Bold, playful, vintage board-game typography: large uppercase letters, strong dimensional
treatment, polished three-dimensional white lettering. GORIPOLY is the dominant element on the
panel and must be spelled exactly GORIPOLY. Never write the word "MONOPOLY" anywhere.

SUBTITLE:
Below the red banner, a smaller silver metallic banner with dark royal-blue uppercase lettering:

KAWALERSKI 2026

BOTTOM STRIP:
At the bottom, integrated into the metallic frame, a narrow horizontal green (#1B7A3E) strip
carrying a small circular gold embossed seal with the intertwined initials GP in the center, and
to its left and right the words "117 KART" and "3-5 GRACZY" in small white uppercase letters.

OVERALL VISUAL DIRECTION:
A luxury collectible board-game box: elegant, humorous, extravagant, celebratory, slightly absurd.
Combine classic vintage board-game illustration, premium vector caricature, Art Deco ornamentation,
rich royal blue with metallic gold, silver and red, dimensional metallic effects, sophisticated
cartoon character design and playful old-school game typography. Symmetrical, centered, highly
polished, visually balanced composition.

PRIORITIES:
1. Preserve the identity and recognizable appearance of the person from the uploaded photos.
2. Keep the same character design, palette and ornament language as the existing card backs.
3. Make GORIPOLY the unmistakable main title.
4. Flat print artwork, full bleed, no 3D mockup.
```

Warianty tego samego promptu na pozostałe panele:

- **tył (57,5 x 88,5 mm)**: to samo tło i ta sama rama, bez postaci. W środku pionowa lista
  zawartości ("117 KART", "28 NIERUCHOMOŚCI", "34 AKCJE", "20 BANKNOTÓW", "8 KART PRZYPAŁU")
  białymi kapitalikami na granacie, u góry mały wordmark GORIPOLY, u dołu złota pieczęć GP.
- **boki (38,5 x 88,5 mm)**: samo tło z pikowanym wzorem, pośrodku pionowy wordmark GORIPOLY
  czytany od dołu do góry, złota linia 1 mm przy obu krawędziach.
- **klapki zamykające (57,5 x 38,5 mm)**: pełna zieleń #1B7A3E z rastrem kropkowym, pośrodku
  złota pieczęć GP.
- **klapka klejowa i klapki pyłowe**: bez grafiki, sama zieleń (nie drukuj tam nic, co ma być widoczne).

## 6. Wymogi techniczne pliku produkcyjnego

- spad 3 mm na zewnętrznych krawędziach rozkroju, wewnątrz rozkroju spadu nie ma
- bezpieczne pole 4 mm od każdej linii zgięcia (grafika przechodzi przez zgięcie, tekst nie)
- 300 dpi w skali 1:1 dla rastrów, ilustracja maskotki min. 1200 px wysokości
- CMYK, czerń tekstowa K100 (nie rich black), hexy z tego dokumentu to wartości ekranowe
- linie cięcia i zgięć na osobnych warstwach, nazwane `CUT` i `FOLD`, nie drukowane
- fonty w krzywych
