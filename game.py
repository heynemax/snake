#!/usr/bin/env python3
"""Snake-Spielengine. Diese Datei musst du NICHT verändern!

Starten:
    python3 game.py             # spielt mit deinem Code aus snake.py
    python3 game.py solution    # spielt mit der Musterlösung aus solution.py

Tasten:
    Pfeiltasten = steuern, R = neu starten, ESC = beenden
"""

import importlib
import sys
from dataclasses import dataclass
from types import ModuleType
from typing import NoReturn, Optional

import pygame

Position = tuple[int, int]
Color = tuple[int, int, int]

CELL: int = 20  # Größe eines Kästchens in Pixeln

KEYS: dict[int, str] = {
    pygame.K_UP: "UP",
    pygame.K_DOWN: "DOWN",
    pygame.K_LEFT: "LEFT",
    pygame.K_RIGHT: "RIGHT",
}


@dataclass
class Game:
    """Der aktuelle Zustand eines Spiels."""

    body: list[Position]
    head: Position
    direction: str
    requested: str
    fruit: Position
    score: int = 0
    over: bool = False


def error(text: str) -> NoReturn:
    print()
    print("FEHLER:", text)
    print()
    pygame.quit()
    sys.exit(1)


def is_position(value: object) -> bool:
    return isinstance(value, (tuple, list)) and len(value) == 2


def new_game(sn: ModuleType) -> Game:
    middle = sn.HEIGHT // 2
    body = [(5, middle), (4, middle), (3, middle), (2, middle)]
    return Game(
        body=body, head=body[0], direction="RIGHT", requested="RIGHT", fruit=sn.random_fruit()
    )


def step(sn: ModuleType, game: Game) -> None:
    """Ein Spielschritt: alle Regeln kommen aus snake.py."""
    game.direction = sn.new_direction(game.direction, game.requested)

    head = sn.next_head(game.head, game.direction)
    if not is_position(head):
        error(f"next_head() muss eine Position (x, y) zurückgeben, nicht {head!r}")
    game.head = (head[0], head[1])

    result = sn.move(game.body, game.head, game.fruit)
    if not (isinstance(result, tuple) and len(result) == 2):
        error(f"move() muss (body, ate) zurückgeben, nicht {result!r}")
    game.body, ate = result

    if ate:
        game.score += 10
        game.fruit = sn.random_fruit()

    if sn.hits_wall(game.head) or sn.bites_itself(game.body):
        game.over = True


def draw_cell(window: pygame.Surface, position: Position, color: Color) -> None:
    x, y = position
    pygame.draw.rect(window, color, pygame.Rect(x * CELL, y * CELL, CELL - 1, CELL - 1))


def show_text(
    window: pygame.Surface,
    text: str,
    size: int,
    color: Color,
    center: Optional[Position] = None,
) -> None:
    font = pygame.font.SysFont(None, size)
    surface = font.render(text, True, color)
    rect = surface.get_rect()
    if center is not None:
        rect.center = center
    window.blit(surface, rect)


def draw(sn: ModuleType, window: pygame.Surface, game: Game) -> None:
    window.fill(sn.COLOR_BACKGROUND)
    draw_cell(window, game.fruit, sn.COLOR_FRUIT)
    for part in game.body:
        draw_cell(window, part, sn.COLOR_SNAKE)
    draw_cell(window, game.head, sn.COLOR_HEAD)

    show_text(window, f"Punkte: {game.score}", 28, (255, 255, 255))

    if game.over:
        width, height = window.get_size()
        show_text(
            window, f"Game Over! Punkte: {game.score}", 60, (255, 0, 0), (width // 2, height // 3)
        )
        show_text(
            window, "R = nochmal, ESC = beenden", 32, (255, 255, 255), (width // 2, height // 2)
        )

    pygame.display.update()


def main() -> None:
    module_name = sys.argv[1] if len(sys.argv) > 1 else "snake"
    sn = importlib.import_module(module_name)

    pygame.init()
    pygame.display.set_caption(f"Snake ({module_name}.py)")
    window = pygame.display.set_mode((sn.WIDTH * CELL, sn.HEIGHT * CELL))
    clock = pygame.time.Clock()
    game = new_game(sn)

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                return
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    pygame.quit()
                    return
                if event.key == pygame.K_r:
                    game = new_game(sn)
                elif event.key in KEYS:
                    game.requested = KEYS[event.key]

        if not game.over:
            step(sn, game)
        draw(sn, window, game)
        clock.tick(sn.SPEED)


if __name__ == "__main__":
    main()
