#!/usr/bin/env python

"""The game of calculating the expression."""

from brain_games.game_engine import start
from brain_games.games import calc


def main():
    """Run Expression calculation brain game."""
    start(calc)


if __name__ == '__main__':
    main()
