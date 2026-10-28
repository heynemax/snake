#!/usr/bin/env python3
"""Überprüft deinen Code in snake.py, Schritt für Schritt.

python3 check.py            # prüft snake.py
python3 check.py solution   # prüft die Musterlösung
"""

import importlib
import sys
from typing import Callable

module_name = sys.argv[1] if len(sys.argv) > 1 else "snake"
sn = importlib.import_module(module_name)

Position = tuple[int, int]


def same(result: object, expected: object, call: str) -> None:
    assert result == expected, f"{call} ergibt {result!r}, erwartet war {expected!r}"


def step_1() -> None:
    same(sn.next_head((5, 5), "RIGHT"), (6, 5), 'next_head((5, 5), "RIGHT")')
    same(sn.next_head((5, 5), "LEFT"), (4, 5), 'next_head((5, 5), "LEFT")')
    same(sn.next_head((5, 5), "UP"), (5, 4), 'next_head((5, 5), "UP")')
    same(sn.next_head((5, 5), "DOWN"), (5, 6), 'next_head((5, 5), "DOWN")')


def step_2() -> None:
    result = sn.move([(5, 5), (4, 5), (3, 5)], (6, 5), (20, 20))
    same(
        result,
        ([(6, 5), (5, 5), (4, 5)], False),
        "move([(5, 5), (4, 5), (3, 5)], (6, 5), (20, 20))",
    )


def step_3() -> None:
    cases: list[tuple[str, str, str]] = [
        ("RIGHT", "UP", "UP"),
        ("RIGHT", "DOWN", "DOWN"),
        ("RIGHT", "RIGHT", "RIGHT"),
        ("RIGHT", "LEFT", "RIGHT"),
        ("LEFT", "RIGHT", "LEFT"),
        ("UP", "DOWN", "UP"),
        ("DOWN", "UP", "DOWN"),
        ("DOWN", "LEFT", "LEFT"),
    ]
    for current, requested, expected in cases:
        same(
            sn.new_direction(current, requested),
            expected,
            f'new_direction("{current}", "{requested}")',
        )


def step_4() -> None:
    w, h = sn.WIDTH, sn.HEIGHT
    cases: list[tuple[Position, bool]] = [
        ((0, 0), False),
        ((w - 1, h - 1), False),
        ((10, 10), False),
        ((-1, 5), True),
        ((w, 5), True),
        ((5, -1), True),
        ((5, h), True),
    ]
    for head, expected in cases:
        same(sn.hits_wall(head), expected, f"hits_wall({head})")


def step_5a() -> None:
    result = sn.move([(5, 5), (4, 5)], (6, 5), (6, 5))
    same(
        result,
        ([(6, 5), (5, 5), (4, 5)], True),
        "move([(5, 5), (4, 5)], (6, 5), (6, 5))",
    )


def step_5b() -> None:
    positions: set[Position] = set()
    for _ in range(500):
        x, y = sn.random_fruit()
        assert 0 <= x < sn.WIDTH and 0 <= y < sn.HEIGHT, f"Obst bei ({x}, {y}) ist außerhalb!"
        positions.add((x, y))
    assert len(positions) > 1, "Das Obst ist immer an derselben Stelle -- ist es zufällig?"


def step_6() -> None:
    same(sn.bites_itself([(5, 5), (4, 5), (3, 5)]), False, "bites_itself([(5, 5), (4, 5), (3, 5)])")
    same(
        sn.bites_itself([(5, 5), (6, 5), (6, 6), (5, 6), (5, 5)]),
        True,
        "bites_itself([(5, 5), (6, 5), (6, 6), (5, 6), (5, 5)])",
    )


STEPS: list[tuple[str, Callable[[], None]]] = [
    ("Schritt 1  (next_head)", step_1),
    ("Schritt 2  (move)", step_2),
    ("Schritt 3  (new_direction)", step_3),
    ("Schritt 4  (hits_wall)", step_4),
    ("Schritt 5a (move: Obst essen)", step_5a),
    ("Schritt 5b (random_fruit)", step_5b),
    ("Schritt 6  (bites_itself)", step_6),
]

if __name__ == "__main__":
    done = 0
    for name, test in STEPS:
        try:
            test()
        except AssertionError as problem:
            print(f"✗ {name}: {problem}")
        except Exception as problem:  # z.B. ein Tippfehler im Code
            print(f"✗ {name}: Fehler im Code -- {type(problem).__name__}: {problem}")
        else:
            print(f"✓ {name}")
            done += 1
    print()
    print(f"{done} von {len(STEPS)} Schritten fertig.")
    if done == len(STEPS):
        print("Super! Alles fertig. Probier doch eine Bonus-Aufgabe aus der README!")
