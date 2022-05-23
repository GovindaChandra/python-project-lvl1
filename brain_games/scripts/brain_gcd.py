#!/usr/bin/env python

"""The game of finding the greatest common divisor."""

from brain_games.game_engine import start
from brain_games.games import gcd


def main():
    """Run greatest common divisior brain game."""
    start(gcd)


if __name__ == '__main__':
    main()
