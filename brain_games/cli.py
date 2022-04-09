"""Welcome functions."""

import prompt


def welcome(game_message):
    """Welcome, request user name, print a greeting and return him.

    Parameters:
        game_message: Describe game rules

    Returns:
        name: User name
    """
    print('\nWelcome to the Brain Games!')
    name = prompt.string('May I have your name? ')
    print('Hello, {0}!\n'.format(name))
    print(game_message)
    return name
