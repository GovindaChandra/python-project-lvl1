#!/usr/bin/env python

"""The game - this number is prime or not."""

from brain_games.game_engine import start
from brain_games.games import prime


def main():
    """Run Is prime brain game."""
    start(prime)


if __name__ == '__main__':
    main()
