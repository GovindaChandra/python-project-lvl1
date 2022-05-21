"""Greatest common divisor game logic."""

import math
import secrets

GAME_RULE = 'Find the greatest common divisor of given numbers.\n'


def game_data_generation():
    """Generate question and correct answer for game.

    Returns:
        return: a tuple of question and correct answer
    """
    secrets_generator = secrets.SystemRandom()
    num1 = secrets_generator.randint(1, 100)
    num2 = secrets_generator.randint(1, 100)
    correct_answer = math.gcd(num1, num2)
    expression = '{0} {1}'.format(num1, num2)
    return expression, str(correct_answer)
