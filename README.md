# Snake -- Schritt für Schritt

Wir programmieren das Spiel Snake. Das Zeichnen und die Tastatur übernimmt
`game.py` -- diese Datei musst du **nicht** anfassen. Du programmierst die
**Regeln** des Spiels in `snake.py`.

Das Spiel läuft von Anfang an. Mit jedem Schritt, den du fertig machst, kann die
Schlange etwas mehr.

```
python3 game.py      # Spiel starten (R = neu starten, ESC = beenden)
python3 check.py     # Prüft, welche Schritte schon richtig sind
```

## Das Spielfeld

Das Spielfeld ist ein Gitter aus Kästchen. Eine Position ist ein Paar `(x, y)`:
`x` ist die Spalte, `y` die Zeile. **Achtung:** `(0, 0)` ist oben links, und `y`
wird nach **unten** größer.

Die Schlange ist eine Liste von Positionen, vorne ist der Kopf:
`[(5, 12), (4, 12), (3, 12)]`.

Die Richtungen heißen `"UP"` (oben), `"DOWN"` (unten), `"LEFT"` (links) und
`"RIGHT"` (rechts).

## Typen

Bei jeder Funktion steht dabei, welche Art von Wert sie bekommt und zurückgibt:

```python
def hits_wall(head: Position) -> bool:
```

heißt: `hits_wall` bekommt eine `Position` und gibt `True` oder `False` (ein
`bool`) zurück. `Position` ist oben in `snake.py` als `tuple[int, int]`
festgelegt, also ein Paar aus zwei ganzen Zahlen.

## Die Schritte

| Schritt | Funktion        | Was passiert danach im Spiel?                                |
|---------|-----------------|--------------------------------------------------------------|
| 0       | --              | Ändere `SPEED` und die Farben oben in `snake.py`.            |
| 1       | `next_head`     | Der Kopf läuft los -- aber der Körper bleibt liegen!         |
| 2       | `move`          | Der Körper folgt dem Kopf.                                   |
| 3       | `new_direction` | Du kannst mit den Pfeiltasten lenken.                        |
| 4       | `hits_wall`     | An der Wand ist das Spiel vorbei.                            |
| 5a      | `move`          | Die Schlange frisst das Obst, wächst und du bekommst Punkte. |
| 5b      | `random_fruit`  | Das Obst erscheint an zufälligen Stellen.                    |
| 6       | `bites_itself`  | Wer sich in den Schwanz beißt, hat verloren.                 |

Lies bei jeder Funktion den Text in den `"""`-Anführungszeichen. Dort steht,
was sie tun soll, mit Beispielen und Tipps.

## Bonus-Aufgaben

- **Durch die Wand:** Statt zu verlieren, kommt die Schlange auf der anderen
  Seite wieder heraus. Tipp: `%` (Rest beim Teilen), z.B. `x % WIDTH`.
- **Immer schneller:** Mit jedem Obst wird die Schlange schneller. Tipp:
  `global SPEED` in `move` und dann `SPEED = SPEED + 1`.
- **Riesenwachstum:** Die Schlange wird pro Obst um 2 Teile länger.

---

## Für Betreuer

- Vorher installieren: `pip install pygame` (oder mit uv ohne Installation:
  `uv run --with pygame game.py`). Python 3.9 oder neuer wird gebraucht.
- `solution.py` ist die Musterlösung. Sie wird **nicht** an die Schüler verteilt.
  `python3 game.py solution` spielt damit, `python3 check.py solution` prüft sie.
- Hängt ein Team fest, kann es eine einzelne Funktion aus `solution.py`
  übernehmen und mit dem nächsten Schritt weitermachen.
- Grober Zeitplan für 60 Minuten:

| Minute | Schritt                                   |
|--------|-------------------------------------------|
| 0--5   | 0: Spiel starten, Tempo und Farben ändern |
| 5--15  | 1: `next_head`                            |
| 15--25 | 2: `move`                                 |
| 25--32 | 3: `new_direction`                        |
| 32--40 | 4: `hits_wall`                            |
| 40--50 | 5a + 5b: Obst                             |
| 50--55 | 6: `bites_itself`                         |
| 55--60 | Bonus / Vorführen                         |

- Zu zweit arbeiten: einer tippt, einer liest vor; bei jedem Schritt wechseln.
