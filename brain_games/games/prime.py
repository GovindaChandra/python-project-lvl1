"""Expression calculation game logic."""

import math
import secrets

from brain_games.game_engine.game_engine import start_game

GAME_RULE = 'Answer "yes" if given number is prime. Otherwise answer "no".\n'


def is_prime(number):
    """Check a given number is prime or not and return True or False.

    Parameters:
        number: Given number

    Returns:
        return: True or False
    """
    upper_bound = math.sqrt(abs(number))
    index = 2
    while index <= upper_bound:
        if number % index == 0:
            return False
        index += 1
    return True


def _game_data_generation():
    secrets_generator = secrets.SystemRandom()
    number = secrets_generator.randint(1, 100)
    correct_answer = 'yes' if is_prime(number) else 'no'
    return str(number), correct_answer


def brain_prime():
    """Start the brain-prime game."""
    start_game(GAME_RULE, _game_data_generation)
