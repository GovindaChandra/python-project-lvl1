"""Expression calculation game logic."""

import random

import prompt

from brain_games.cli import username_request, welcome_user
from brain_games.game_settings import GAME_OVER, GAME_WIN, NUMBER_OF_QUESTIONS


def _calc(args):
    if args[2] == '+':
        return args[0] + args[1]
    elif args[2] == '-':
        return args[0] - args[1]
    elif args[2] == '*':
        return args[0] * args[1]


def _operands_gen():
    return (random.randint(1, 100),  # noqa: S311
        random.randint(1, 100),  # noqa: S311
        random.choice(('+', '-', '*')),  # noqa: S311
    )


def expression_calc():
    """Greeting, name request, the game itself."""
    welcome_user()
    print('What is the result of the expression?.\n')
    name = username_request()

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
