"""Expression calculation game logic."""

import math
import secrets

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


def game_data_generation():
    """Generate question and correct answer for game.

    Returns:
        return: a tuple of question and correct answer
    """
    secrets_generator = secrets.SystemRandom()
    number = secrets_generator.randint(1, 100)
    correct_answer = 'yes' if is_prime(number) else 'no'
    return str(number), correct_answer
