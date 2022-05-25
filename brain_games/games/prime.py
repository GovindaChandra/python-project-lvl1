"""Is prime? - game logic."""

import math
import random

RULE = 'Answer "yes" if given number is prime. Otherwise answer "no".\n'


def is_prime(number):
    """Check a given number is prime or not and return True or False.

    Parameters:
        number: Given number

    Returns:
        return: True or False
    """
    if number < 2:
        return False
    upper_bound = math.sqrt(number)
    index = 2
    while index <= upper_bound:
        if number % index == 0:
            return False
        index += 1
    return True


def data_generation():
    """Generate question and correct answer for game.

    Returns:
        return: a tuple of question and correct answer
    """
    number = random.randint(1, 100)
    correct_answer = 'yes' if is_prime(number) else 'no'
    return number, correct_answer
