"""Is even? - game logic."""

import random

from brain_games.games.game_settings import start_game


def _brain_even_game_function():
    number = random.randint(1, 100)  # noqa: S311
    correct_answer = 'yes' if number % 2 == 0 else 'no'
    return str(number), correct_answer


def brain_even():
    """Start the brain-even game."""
    game_rule = 'Answer "yes" if number is even, otherwise answer "no".\n'
    start_game(game_rule, _brain_even_game_function)
