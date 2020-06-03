"""Expression calculation game logic."""

import random

import prompt

from brain_games.cli import username_request, welcome_user

from brain_games.game_settings import NUMBER_OF_QUESTIONS, GAME_OVER, GAME_WIN


def _operators():
    return random.choice('+', '-', '*')  # noqa: S311


def expression_calc():
    """Greeting, name request, the game itself."""
    welcome_user()
    print('What is the result of the expression?.\n')
    name = username_request()

    for step in range(NUMBER_OF_QUESTIONS):
        operand_1 = random.randint(1, 100)  # noqa: S311
        operand_2 = random.randint(1, 100)  # noqa: S311
        operator = random.choice('+', '-', '*')  # noqa: S311
        print('Question:', operand_1, operator, operand_2)
        answer = prompt.string('Your answer: ')
        if answer == _is_c(number):
            print('Correct!')
            if step == NUMBER_OF_QUESTIONS - 1:
                print(GAME_WIN.format(name))
        else:
            print(GAME_OVER.format(answer, 'yes' if answer == 'no' else 'no'))
            print("Let's try again, {0}!\n".format(name))
            break
