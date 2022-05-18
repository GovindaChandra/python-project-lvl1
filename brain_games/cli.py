"""Welcome functions."""

import prompt


def welcome_user():
    """Welcome, request user name, print a greeting and return him.

    Returns:
        name: User name
    """
    print('\nWelcome to the Brain Games!')
    name = prompt.string('May I have your name? ')
    print('Hello, {0}!\n'.format(name))
    return name
