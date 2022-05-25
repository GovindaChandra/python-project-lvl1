"""Expression calculation game logic."""

import random

RULE = 'What is the result of the expression?\n'


def _calc(num1, num2, operator):
    if operator == '+':
        return num1 + num2
    elif operator == '-':
        return num1 - num2
    elif operator == '*':
        return num1 * num2


def data_generation():
    """Generate question and correct answer for game.

    Returns:
        return: a tuple of question and correct answer
    """
    num1 = random.randint(1, 100)
    num2 = random.randint(1, 100)
    operator = random.choice(('+', '-', '*'))
    correct_answer = _calc(num1, num2, operator)
    question = f'{num1} {operator} {num2}'
    return question, str(correct_answer)
