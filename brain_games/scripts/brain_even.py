#!/usr/bin/env python

"""The game - this number is even or not."""

from brain_games.game_engine import start
from brain_games.games import even


def main():
    """Run IS even brain game."""
    start(even)


if __name__ == '__main__':
    main()
