"""Expression calculation game logic."""

import random

from brain_games.games.game_settings import start_game


def _calc(operands):
    if operands[1] == '+':
        return operands[0] + operands[2]
    elif operands[1] == '-':
        return operands[0] - operands[2]
    elif operands[1] == '*':
        return operands[0] * operands[2]


def _brain_calc_game_function():
    first_op = random.randint(1, 100)  # noqa: S311
    second_op = random.randint(1, 100)  # noqa: S311
    ops_sign = random.choice(('+', '-', '*'))  # noqa: S311
    correct_answer = _calc((first_op, ops_sign, second_op))
    expression = '{0} {1} {2}'.format(first_op, ops_sign, second_op)
    return expression, str(correct_answer)


def brain_calc():
    """Start the brain-calc game."""
    game_rule = 'What is the result of the expression?\n'
    start_game(game_rule, _brain_calc_game_function)
