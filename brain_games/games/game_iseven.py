"""Is even? - game logic."""

import random

from brain_games.games.game_settings import game_engine


def _brain_even_game_function():
    number = random.randint(1, 100)  # noqa: S311
    answer = 'yes' if number % 2 == 0 else 'no'
    return str(number), answer


def brain_even():
    """Start the game."""
    game_rule = 'Answer "yes" if number is even, otherwise answer "no".\n'
    game_engine(game_rule, _brain_even_game_function)
