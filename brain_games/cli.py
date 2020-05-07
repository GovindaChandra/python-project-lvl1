#!/usr/bin/env python

import prompt


def welcome_user():
    print('\nWelcome to the Brain Games!\n')
    name = prompt.string('May I have your name? ')
    print('Hello, {0}!\n'.format(name))


if __name__ == '__main__':
    welcome_user()
