"""Miscellaneous functions."""

import prompt


def welcome_user():
    """Welcome user function."""
    print('\nWelcome to the Brain Games!')


def get_name():
    """Request user name and return him.

    Returns:
        User name.
    """
    name = prompt.string('May I have your name? ')
    print('Hello, {0}!\n'.format(name))
    return name
