"""Miscellaneous functions."""

import prompt


def welcome_user():
    """Welcome to Brain Games function."""
    print('\nWelcome to the Brain Games!')


def username_request():
    """Request user name, print a greeting and return him.

    Returns:
        User name.
    """
    name = prompt.string('May I have your name? ')
    print('Hello, {0}!\n'.format(name))
    return name
