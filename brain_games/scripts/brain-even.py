#!/usr/bin/env python

"""Game the correct answer is an even or odd number."""

import cli
import random
import prompt

NUMBER_OF_QUESTIONS = 3
DICT_OF_ANSWERS = {'yes': 'no', 'no': 'yes'}
GAME_OVER = "'{0}' is wrong answer ;(. Correct answer was '{1}'."
GAME_WIN = 'Congratulations, {0}!'

def _is_even(number):
    return "yes" if number % 2 == 0 else "no"

def brain_even():
    """Greeting, name request, the game itself."""
    cli.welcome_user()
    print('Answer "yes" if number even otherwise answer "no".\n')
    name = cli.get_name()
    
    for step in range(NUMBER_OF_QUESTIONS):
        number = random.randint(1, 100)
        print('Question:', number)
        answer = prompt.string('Your answer: ')
        if answer == _is_even(number):
            print('Correct!')
            if step == NUMBER_OF_QUESTIONS - 1:
                print(GAME_WIN.format(name))
        else:
            print(GAME_OVER.format(answer, DICT_OF_ANSWERS[answer]))
            print('Let\'s try again, {0}!\n'.format(name))
            break

def main():
    """Run brain even game."""
    brain_even()


if __name__ == '__main__':
    main()
