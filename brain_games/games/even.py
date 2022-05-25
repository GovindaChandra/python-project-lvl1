"""Is even? - game logic."""

import random

RULE = 'Answer "yes" if number is even, otherwise answer "no".\n'


def data_generation():
    """Generate question and correct answer for game.

    Returns:
        return: a tuple of question and correct answer
    """
    number = random.randint(1, 100)
    correct_answer = 'yes' if number % 2 == 0 else 'no'
    return number, correct_answer
