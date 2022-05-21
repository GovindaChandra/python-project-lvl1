#!/usr/bin/env python

"""Game this number is even or not."""

from brain_games.game_engine import start_game
from brain_games.games import iseven


def main():
    """Run IS even brain game."""
    start_game(iseven)


if __name__ == '__main__':
    main()
