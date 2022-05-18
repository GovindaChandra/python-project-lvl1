"""Greatest common divisor game logic."""

import math
import secrets

from brain_games.game_engine.game_engine import start_game

GAME_RULE = 'Find the greatest common divisor of given numbers.\n'


def _game_data_generation():
    secrets_generator = secrets.SystemRandom()
    num1 = secrets_generator.randint(1, 100)
    num2 = secrets_generator.randint(1, 100)
    correct_answer = math.gcd(num1, num2)
    expression = '{0} {1}'.format(num1, num2)
    return expression, str(correct_answer)


def brain_gcd():
    """Start the brain-gcd game."""
    start_game(GAME_RULE, _game_data_generation)
