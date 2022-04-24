"""Welcome functions."""

import prompt


def welcome(game_rule):
    """Welcome, request user name, print a greeting and return him.

    Parameters:
        game_rule: Describe game rules

    Returns:
        name: User name
    """
    print('\nWelcome to the Brain Games!')
    name = prompt.string('May I have your name? ')
    print('Hello, {0}!\n'.format(name))
    print(game_rule)
    return name
