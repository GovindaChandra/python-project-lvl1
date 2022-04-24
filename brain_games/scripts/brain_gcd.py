"""Greatest common divisor game logic."""

import math
import random

from brain_games.games.game_settings import game_engine


def _brain_gcd_game_function():
    first_op = random.randint(1, 100)  # noqa: S311
    second_op = random.randint(1, 100)  # noqa: S311
    correct_answer = math.gcd(first_op, second_op)
    expression = '{0} {1}'.format(first_op, second_op)
    return expression, str(correct_answer)


def brain_gcd():
    """Start the brain-gcd game."""
    game_rule = 'Find the greatest common divisor of given numbers.\n'
    game_engine(game_rule, _brain_gcd_game_function)
