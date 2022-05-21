"""Expression calculation game logic."""

import random

GAME_RULE = 'What is the result of the expression?\n'


def _calc(num1, num2, operator):
    if operator == '+':
        return num1 + num2
    elif operator == '-':
        return num1 - num2
    elif operator == '*':
        return num1 * num2


def game_data_generation():
    """Generate question and correct answer for game.

    Returns:
        return: a tuple of question and correct answer
    """
    random_generator = random.Random()
    num1 = random_generator.randint(1, 100)
    num2 = random_generator.randint(1, 100)
    operator = random_generator.choice(('+', '-', '*'))
    correct_answer = _calc(num1, num2, operator)
    return '{0} {1} {2}'.format(num1, operator, num2), str(correct_answer)
