"""Expression calculation game logic."""

import random

import prompt

from brain_games.cli import welcome
from brain_games.game_settings import GAME_OVER, GAME_WIN, NUMBER_OF_QUESTIONS


def _calc(operands):
    if operands[2] == '+':
        return operands[0] + operands[1]
    elif operands[2] == '-':
        return operands[0] - operands[1]
    elif operands[2] == '*':
        return operands[0] * operands[1]


def _operands_gen():
    first_op = random.randint(1, 100)  # noqa: S311
    second_op = random.randint(1, 100)  # noqa: S311
    ops_sign = random.choice(('+', '-', '*'))  # noqa: S311
    return (first_op, second_op, ops_sign)


def brain_calc():
    """Brain calc game logic."""
    name = welcome('What is the result of the expression?\n')

    for step in range(NUMBER_OF_QUESTIONS):
        operands = _operands_gen()
        print('Question:', operands[0], operands[2], operands[1])
        answer = prompt.integer('Your answer: ')
        if answer == _calc(operands):
            print('Correct!')
            if step == NUMBER_OF_QUESTIONS - 1:
                print(GAME_WIN.format(name))
        else:
            print(GAME_OVER.format(answer, _calc(operands)))
            print("Let's try again, {0}!\n".format(name))
            break
