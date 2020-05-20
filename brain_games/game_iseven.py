"""Is even? - game logic."""

import random

import prompt

import cli

NUMBER_OF_QUESTIONS = 3
GAME_OVER = "'{0}' is wrong answer ;(. Correct answer was '{1}'."
GAME_WIN = 'Congratulations, {0}!'


def _is_even(number):
    return 'yes' if number % 2 == 0 else 'no'


def brain_even():
    """Greeting, name request, the game itself."""
    cli.welcome_user()
    print('Answer "yes" if number even otherwise answer "no".\n')
    name = cli.get_name()

    for step in range(NUMBER_OF_QUESTIONS):
        number = random.randint(1, 100)  # noqa: S311
        print('Question:', number)
        answer = prompt.string('Your answer: ')
        if answer == _is_even(number):
            print('Correct!')
            if step == NUMBER_OF_QUESTIONS - 1:
                print(GAME_WIN.format(name))
        else:
            print(GAME_OVER.format(answer, 'yes' if answer == 'no' else 'no'))
            print("Let's try again, {0}!\n".format(name))
            break