"""Expression calculation game logic."""

import math
import random

from brain_games.game_engine.game_engine import start_game


def _is_prime(number):
    upper_bound = math.sqrt(number)
    index = 2
    while index <= upper_bound:
        if number % index == 0:
            return False
        index += 1
    return True


def _brain_prime_game_function():
    number = random.randint(4, 100)  # noqa: S311
    correct_answer = 'yes' if _is_prime(number) else 'no'
    return str(number), correct_answer


def brain_prime():
    """Start the brain-prime game."""
    rule = 'Answer "yes" if given number is prime. Otherwise answer "no".\n'
    start_game(rule, _brain_prime_game_function)
