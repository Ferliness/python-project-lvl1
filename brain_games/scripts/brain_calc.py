#!/usr/bin/env python
"""Run Brain Games."""

from brain_games.engine import run_game
from brain_games.games import calc


def main():
    """Start the game."""
    run_game(calc)


if __name__ == '__main__':
    main()
