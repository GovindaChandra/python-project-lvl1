"""Arithmetic progression game logic."""

import random

from brain_games.games.game_settings import start_game


def _brain_progression_game_function():
    count_nums = random.randint(5, 10)  # noqa: S311
    first_num = random.randint(1, 100)  # noqa: S311
    diff = random.randint(1, count_nums)  # noqa: S311
    diff *= random.choice([-1, 1])  # noqa: S311
    progression = list(range(first_num, first_num + count_nums * diff, diff))
    correct_answer = progression[abs(diff) - 1]
    progression[abs(diff) - 1] = '..'
    return ' '.join(map(str, progression)), str(correct_answer)


def brain_progression():
    """Start the brain-gcd game."""
    game_rule = 'What number is missing in the progression?\n'
    start_game(game_rule, _brain_progression_game_function)
