"""Hier programmierst DU die Regeln von Snake!

Das Spielfeld ist ein Gitter aus Kästchen: WIDTH Spalten und HEIGHT Zeilen.
Eine Position ist ein Paar (x, y):
    - x ist die Spalte (0 = ganz links)
    - y ist die Zeile  (0 = ganz oben!  y wird nach UNTEN größer)

Die Schlange ist eine Liste von Positionen. Das erste Element ist der Kopf:
    body = [(5, 12), (4, 12), (3, 12)]   # Kopf bei (5, 12)

Richtungen sind die Texte "UP" (oben), "DOWN" (unten), "LEFT" (links) und "RIGHT" (rechts).

Typen: Hinter jedem Parameter steht, welche Art von Wert er bekommt, und hinter
dem Pfeil ->, was die Funktion zurückgibt. Zum Beispiel bedeutet
    def hits_wall(head: Position) -> bool:
"hits_wall bekommt eine Position und gibt True oder False zurück".

Spiel starten:      python3 game.py
Code überprüfen:    python3 check.py
"""

import random  # noqa: F401  (wird erst in Schritt 5b gebraucht)

# Eigene Namen für Typen, damit man sofort sieht, was gemeint ist:
Position = tuple[int, int]  # (x, y)
Direction = str  # "UP", "DOWN", "LEFT" oder "RIGHT"
Color = tuple[int, int, int]  # (Rot, Grün, Blau), je 0 bis 255

WIDTH: int = 36
HEIGHT: int = 24

# ---------- Schritt 0: Zum Aufwärmen ----------
# Starte das Spiel. Ändere dann das Tempo und die Farben.
SPEED: int = 8
COLOR_BACKGROUND: Color = (0, 0, 0)
COLOR_SNAKE: Color = (0, 200, 0)
COLOR_HEAD: Color = (150, 255, 150)
COLOR_FRUIT: Color = (255, 0, 0)


# ---------- Schritt 1: Der Kopf bewegt sich ----------
def next_head(head: Position, direction: Direction) -> Position:
    """Gib die neue Position des Kopfes zurück, wenn er ein Kästchen
    in die Richtung `direction` geht.

    Beispiel: next_head((5, 5), "RIGHT") ergibt (6, 5)
              next_head((5, 5), "UP")    ergibt (5, 4)

    Tipp: x, y = head   holt x und y aus der Position heraus.
    """
    # TODO
    return head


# ---------- Schritt 2: Der Körper folgt dem Kopf ----------
# ---------- Schritt 5a: Obst essen ----------
def move(body: list[Position], head: Position, fruit: Position) -> tuple[list[Position], bool]:
    """Bewege die Schlange: der neue Kopf kommt vorne an die Liste,
    das letzte Teil (der Schwanz) fällt weg.

    Gib zwei Dinge zurück:  return body, ate
    `ate` ist True, wenn der Kopf auf dem Obst gelandet ist, sonst False.

    Schritt 2:  Kümmere dich erst nur ums Bewegen (ate ist immer False).
    Schritt 5a: Wenn der Kopf auf dem Obst ist, fällt der Schwanz NICHT weg.
                So wird die Schlange länger!

    Tipp: body.insert(0, head)  fügt vorne ein,
          body.pop()            entfernt das letzte Element.
    """
    # TODO
    return body, False


# ---------- Schritt 3: Lenken (aber nicht umdrehen!) ----------
def new_direction(current: Direction, requested: Direction) -> Direction:
    """Gib zurück, in welche Richtung die Schlange als Nächstes läuft.

    `current` ist die Richtung, in die sie gerade läuft,
    `requested` ist die Pfeiltaste, die zuletzt gedrückt wurde.

    Die Schlange darf sich nicht umdrehen: Läuft sie nach "RIGHT",
    darf sie nicht direkt nach "LEFT". Dann läuft sie einfach weiter.

    Beispiel: new_direction("RIGHT", "UP")   ergibt "UP"
              new_direction("RIGHT", "LEFT") ergibt "RIGHT"
    """
    # TODO
    return current


# ---------- Schritt 4: Die Wand ----------
def hits_wall(head: Position) -> bool:
    """Gib True zurück, wenn der Kopf außerhalb des Spielfelds ist, sonst False.

    Das Spielfeld geht von x = 0 bis x = WIDTH - 1
    und von y = 0 bis y = HEIGHT - 1.
    """
    # TODO
    return False


# ---------- Schritt 5b: Obst an zufälliger Stelle ----------
def random_fruit() -> Position:
    """Gib eine zufällige Position (x, y) innerhalb des Spielfelds zurück.

    Tipp: random.randint(0, 10) ergibt eine Zufallszahl von 0 bis einschließlich 10.
    """
    # TODO
    return (WIDTH // 2, HEIGHT // 2)


# ---------- Schritt 6: Nicht in den eigenen Schwanz beißen! ----------
def bites_itself(body: list[Position]) -> bool:
    """Gib True zurück, wenn der Kopf (body[0]) auf einem anderen Teil
    der Schlange liegt, sonst False.

    Tipp: body[1:] ist die Liste ohne das erste Element.
          `a in my_list` prüft, ob a in der Liste vorkommt.
    """
    # TODO
    return False
