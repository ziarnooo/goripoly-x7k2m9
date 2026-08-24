# GORIPOLY - specyfikacja do drukarni

Wszystko w tym katalogu generuje `build-druk.sh` z `karty.html`. Po każdej zmianie w kartach:

```bash
bash druk/build-druk.sh          # przebudowuje 4 PDF-y i robi kontrolę formatu
```

## 1. Co wysyłamy do drukarni

| Plik | Co to jest | Stron |
|---|---|---|
| `GORIPOLY-fronty-naklad.pdf` | awersy, **1 strona = 1 fizyczna karta**, wszystkie kopie wg nakładu | 117 |
| `GORIPOLY-rewers.pdf` | rewers, jeden wzór na całą talię | 1 |
| `GORIPOLY-fronty-wzory.pdf` | tylko unikalne wzory, do korekty i wyceny (nie do produkcji) | 82 |
| `GORIPOLY-proof-A4.pdf` | 9 kart na A4 ze znacznikami cięcia, do wydruku domowego na próbę | 14 |

Do drukarni idą **dwa pierwsze pliki**. Impozycję (rozłożenie na arkusz) robi drukarnia u siebie,
dlatego w plikach produkcyjnych nie ma znaczników cięcia.

## 2. Format

| Parametr | Wartość |
|---|---|
| Netto (linia cięcia) | 56 x 87 mm, pionowo |
| Spad | 3 mm z każdej strony |
| Strona PDF | 62 x 93 mm (netto + spad) |
| Strefa bezpieczna | 3,5 mm od linii cięcia - tam siedzi czarny keyline kart |
| Zaokrąglenie narożników | 3 mm (wykrojnik) |
| Liczba kart | 117 (109 talia podstawowa + 8 kart przypału) |

Realny MediaBox w PDF-ach to **62,06 x 93,13 mm** - Chrome zaokrągla milimetry do pikseli.
Odchyłka wychodzi 0,03 mm na krawędź cięcia, czyli kilkanaście razy mniej niż tolerancja krajarki.
Drukarnia skaluje do swojego formatu albo centruje - obie drogi są bezpieczne.

## 3. Nakład

| Typ | Sztuk | Unikalnych wzorów |
|---|---|---|
| Nieruchomości | 28 | 28 |
| Jokery (property wild) | 11 | 8 |
| Czynsze | 13 | 6 |
| Akcje | 29 | 19 |
| Budynki | 5 | 4 |
| Karty przypału | 8 | 8 |
| Pieniądze | 20 | 6 |
| Karty zasad | 3 | 3 |
| **Awersy razem** | **117** | **82** |
| Rewers | 117 (ten sam wzór) | 1 |

## 4. Papier i uszlachetnienie

- karton do kart do gry **300 g**, najlepiej z warstwą blue/black core (nie prześwituje przy rozdaniu)
- **folia mat dwustronnie** albo laminat soft-touch - bez folii karty kleją się i szybko brudzą
- wykrojnik z promieniem 3 mm
- grubość jednej karty po laminowaniu jest potrzebna do wymiarów pudełka - patrz `../PUDELKO.md`,
  poproś drukarnię o tę liczbę w wycenie

## 5. Kolor - do ustalenia przy zamówieniu

PDF-y wychodzą z przeglądarki, więc są w **RGB (sRGB/ICCBased)**, nie w CMYK. Do wyboru:

1. **Drukarnia konwertuje** na swój profil maszyny - najprostsze i przy jednym egzemplarzu
   wystarczające. Trzeba tylko powiedzieć wprost, że pliki są w RGB.
2. **Konwersja u nas** w Acrobat DC (Preflight -> Convert to PDF/X-1a, profil od drukarni)
   albo w Illustratorze. Wtedy dochodzi kontrola czerni: teksty mają `#111111`, po konwersji
   złożą się jako composite black. Jeśli drukarnia chce K100 na tekstach, robimy to w tym kroku.

Kolory nasycone (`#F5E23A` żółty, `#17A24A` zielony, `#E1231C` czerwony) zjadą w CMYK.
To jest normalne i nie psuje gry, bo karty rozróżnia też kształt piktogramu i nazwa zestawu,
nie sam odcień.

## 6. Rewers - jak jest zbudowany

Grafika rewersu (`rewers.jpg`, 860 x 1340 px) ma **własną ramkę na samej krawędzi i zero spadu**.
Rozciągnięta na cały element 62 x 93 mm oddałaby złotą ramkę krajarce. Dlatego w `karty.css`
grafika ma 58 x 89 mm (1 mm zapasu za linią cięcia z każdej strony), a spad dopełnia granat
`#12294A`, dokładnie w kolorze zewnętrznej obwoluty grafiki. Białe narożniki źródłowego JPG
obcina promień 2,4 mm.

Efektywna rozdzielczość: 860 px na 58 mm = **377 dpi**, czyli powyżej wymaganych 300.
Rewers jest rastrem, nie wektorem. Przy druku cyfrowym jednego egzemplarza to nie problem;
gdyby drukarnia wymagała wektorów, ornament trzeba przerysować.

## 7. Kontrola przed wysyłką

`build-druk.sh` na końcu odpala `kontrola.py`, które sprawdza:

- format każdej strony (musi być 62 x 93 mm, tolerancja 0,3 mm),
- liczbę stron (117 / 1 / 82 / 14),
- czy **Poppins** jest osadzony w PDF. Font leci z Google Fonts po sieci, więc build bez
  internetu podstawi Montserrat i skład się rozjedzie. Jeśli kontrola krzyknie o Poppinsa,
  przebuduj z siecią, nie wysyłaj takiego pliku.

Do tego wzrokowo, przed wysyłką:

- otwórz `GORIPOLY-proof-A4.pdf`, wydrukuj jedną stronę bez skalowania i przyłóż linijkę:
  karta między liniami cięcia musi mieć 56 x 87 mm,
- przejrzyj `GORIPOLY-fronty-wzory.pdf` (82 strony) - to jest ostatni moment na literówki,
- sprawdź, czy nic ważnego nie leży bliżej niż 3,5 mm od linii cięcia.
