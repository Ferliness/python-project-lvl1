#!/usr/bin/env python
"""Run Brain Games."""

from brain_games.engine import run_game
from brain_games.games import progression


def main():
    """Start the game."""
    run_game(progression)


if __name__ == '__main__':
    main()
