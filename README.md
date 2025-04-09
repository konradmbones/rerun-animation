# Rerun Animation Viewer

Ten projekt umożliwia wizualizację animacji SMPL w formacie NPZ przy użyciu biblioteki rerun-sdk.

## Wymagania systemowe

- Python 3.10
- pip (menedżer pakietów Python)
- Virtualenv (opcjonalnie, ale zalecane)

## Instalacja

1. Utwórz i aktywuj wirtualne środowisko Python:
```bash
python3.10 -m venv venv
source venv/bin/activate  # dla Linux/Mac
# lub
.\venv\Scripts\activate  # dla Windows
```

2. Zainstaluj wymagane biblioteki:
```bash
pip install -r requirements.txt
```

## Struktura projektu

```
.
├── README.md
├── requirements.txt
├── bin/
│   └── rerun-animation.ini  # Konfiguracja dla rerun-animation
├── convert/
│   └── convert_npz_final.py  # Skrypt do konwersji plików NPZ
└── npz_models/
    ├── original/            # Oryginalne pliki NPZ
    └── converted_models/    # Przekonwertowane pliki NPZ
```

## Użycie

1. Konwersja plików NPZ:
```bash
python convert/convert_npz_final.py
```

2. Uruchomienie wizualizacji:
```bash
rerun-animation npz_models/converted_models/nazwa_pliku.npz
```

## Konfiguracja

Plik `bin/rerun-animation.ini` zawiera konfigurację wizualizacji:
- Typ modelu (SMPL)
- Format pozy (axis-angle)
- Kolory i ustawienia wizualizacji
- Mapowanie kluczy danych

## Rozwiązywanie problemów

1. Jeśli widzisz tylko szkielet bez mesha:
   - Upewnij się, że używasz przekonwertowanego pliku NPZ
   - Sprawdź czy plik konfiguracyjny jest w katalogu `bin`
   - Upewnij się, że opcja `show_mesh = yes` jest ustawiona w konfiguracji

2. Jeśli występują błędy z pose_blendshapes:
   - Sprawdź czy plik NPZ został prawidłowo przekonwertowany
   - Upewnij się, że używasz prawidłowego modelu SMPL

## Zależności

Główne zależności projektu:
- rerun-sdk==0.22.1
- rerun-animation==0.1.4
- numpy==2.2.4
- colour==0.1.5

Pełna lista zależności znajduje się w pliku `requirements.txt`.
