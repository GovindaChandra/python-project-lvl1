"""Now just one function - welcome_user()."""

import prompt


def welcome_user():
    """Welcome user function."""
    print('\nWelcome to the Brain Games!\n')
    name = prompt.string('May I have your name? ')
    print('Hello, {0}!\n'.format(name))
