"""Is even? - game logic."""

import random

import prompt

from brain_games.cli import welcome
from brain_games.games.game_settings import (
    GAME_OVER,
    GAME_WIN,
    NUMBER_OF_QUESTIONS,
)


def _is_even(number):
    return 'yes' if number % 2 == 0 else 'no'


def _number_gen():
    return random.randint(1, 100)  # noqa: S311


def brain_even():
    """Brain even game logic."""
    name = welcome('Answer "yes" if number is even, otherwise answer "no".\n')

    for step in range(NUMBER_OF_QUESTIONS):
        number = _number_gen()
        print('Question:', number)
        answer = prompt.string('Your answer: ')
        if answer == _is_even(number):
            print('Correct!')
            if step == NUMBER_OF_QUESTIONS - 1:
                print(GAME_WIN.format(name))
        else:  # 'yes' if answer == 'no' else 'no'
            print(GAME_OVER.format(answer, _is_even(number)))
            print("Let's try again, {0}!\n".format(name))
            break
