# Garden-Simulator

Der Garden-Simulator ist ein einfaches Python-Programm, das einen Garten als 5×5-Raster darstellt. Du kannst darin Pflanzen anbauen und ernten.

Der Befehl `show` zeigt die Zeilen- und Spaltennummern des Gartens an.

```text
     0   1   2   3   4
  +---+---+---+---+---+
 0| . | o |   |   |   |
  +---+---+---+---+---+
 1|   |   |   |   |   |
  +---+---+---+---+---+
 2|   |   | . |   |   |
  +---+---+---+---+---+
 3|   |   |   | o |   |
  +---+---+---+---+---+
 4|   |   |   |   | R |
  +---+---+---+---+---+
```

Die Symbole im Raster bedeuten:

- Leerzeichen: ein leeres Feld
- `o`: ein umgegrabenes Feld
- `.`: ein gepflanzter Samen 
- `R`: eine reife Pflanze, die geerntet werden kann

## Verfügbare Befehle

- `show`
- `dig row col`
- `plant row col crop`
- `water row col`
- `day`
- `harvest row col`
- `help`
- `quit`

## Garden-Simulator starten

Führe im Hauptverzeichnis des Projekts folgenden Befehl aus:

```bash
python main.py
```

Alternativ kannst du `make` verwenden:

```bash
make run
```

## Aufbau des Codes

Die Regeln des Garden-Simulators befinden sich in `garden.py`. Diese Datei verwendet einfache Funktionen und grundlegende Programmierkonzepte. Die meisten Aufgaben erfordern Änderungen in dieser Datei.

Die Kommandozeilenoberfläche (CLI) befindet sich in `main.py`. Sie liest die eingegebenen Befehle, zerlegt sie in einzelne Wörter und entscheidet mit `if`/`else`, welche Aktion ausgeführt wird. Die Datei `main.py` muss auch im Zuge der Aufgaben editiert werden.

Die Darstellung des Gartens befindet sich in `cli_view.py`. Die Klasse `GardenPrinter` wandelt die Gartendaten in ein ASCII-Raster um, das im Terminal ausgegeben wird. Diese Daten dürfen nicht verändert werden.

Der Test-Runner für die Aufgaben befindet sich in `test_runner.py`. Er prüft jede Aufgabe und zeigt deutlich an, welche Tests bestanden wurden und wo noch Änderungen notwendig sind.

## Datenmodell

Jedes Feld im Garten ist ein Dictionary mit folgenden Einträgen:

- `state`: `"empty"`, `"hole"`, `"seed"` oder `"ripe"`
- `crop`: `None` oder ein String
- `water`: eine ganze Zahl (Int)
- `days_as_seed`: eine ganze Zahl (Int)

## Regeln

- `dig` ist nur auf einem Feld mit dem Zustand `empty` erlaubt und ändert den Zustand zu `hole`.
- `plant` ist nur auf einem Feld mit dem Zustand `hole` erlaubt. Der Zustand wird zu `seed`, `crop` wird gesetzt und `water` sowie `days_as_seed` werden auf `0` gesetzt.
- `water` ist nur auf einem Feld mit dem Zustand `seed` erlaubt und erhöht den Wasserstand höchstens bis `WATER_MAX`.
- `day` wirkt sich gleichzeitig auf alle Felder aus:
  - Der Wasserstand wird um `1` verringert.
  - Das Wachstum ist vorhersehbar:
    - Ein ausreichend bewässerter `seed` erhält einen Wachstumstag.
    - Nach `RIPE_DAYS_FROM_SEED` Wachstumstagen wird aus `seed` der Zustand `ripe`.
- `harvest` ist nur bei einer reifen Pflanze erlaubt, gibt den Namen der Pflanze zurück und setzt das Feld auf `empty` zurück.
- Beim Ernten einer `tomato` wird zusätzlich eine Zeile an `harvests/tomato.txt` angehängt.

## Arbeiten mit generativer KI

Verwende ausschließlich ein chatbasiertes KI-Produkt.

Nutze die KI wie einen persönlichen Programmierpartner, der dir bei Fragen zu Syntax, Logik oder Programmabläufen hilft.

## Tutorial 1: Neuen Code hinzufügen

Öffne `main.py`. In der Funktion `main()` findest du folgende Zeile:

```python
print("Garden Simulator")
```

Ersetze sie durch:

```python
print("Garden Simulator by <Dein Name>")  # Beispiel: print("Garden Simulator by Tobias")
```

Speichere die Datei mit `CTRL+S`.

Starte anschließend den Garden-Simulator:

```bash
python main.py
```

Alternativ:

```bash
make run
```

## Tutorial 2: Tests ausführen

Starte den Test-Runner mit:

```bash
python test_runner.py
```

Alternativ kannst du den Test-Runner mit `make` starten:

```bash
make test
```

Jeder Test zeigt `[PASS]` oder `[FAIL]` an. Alle sechs erforderlichen Tests müssen bestanden werden, einschließlich der beiden Wachstumstests für Aufgabe 5.
