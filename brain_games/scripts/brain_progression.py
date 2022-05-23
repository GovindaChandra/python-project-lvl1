#!/usr/bin/env python

"""The game of finding a member of an arithmetic progression."""

from brain_games.game_engine import start
from brain_games.games import progression


def main():
    """Run finding a member of an progressin brain game."""
    start(progression)


if __name__ == '__main__':
    main()
