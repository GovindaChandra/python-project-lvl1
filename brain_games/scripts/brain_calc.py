#!/usr/bin/env python

"""The game of calculating the expression."""

from brain_games.game_engine import start_game
from brain_games.games import expression


def main():
    """Run Expression calculation brain game."""
    start_game(expression)


if __name__ == '__main__':
    main()
