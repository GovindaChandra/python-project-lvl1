"""Global settings for games."""

import prompt

NUMBER_OF_ROUNDS = 3
GAME_OVER = "'{0}' is wrong answer ;(. Correct answer was '{1}'."


def start_game(game_rule, game_data_function):
    """Print greeting, lunch game function.

    Parameters:
        game_rule: Describe game rules
        game_data_function: game logic and data generation function
    """
    print('\nWelcome to the Brain Games!')
    name = prompt.string('May I have your name? ')
    print('Hello, {0}!\n'.format(name))
    print(game_rule)
    for _ in range(NUMBER_OF_ROUNDS):
        expression, correct_answer = game_data_function()
        print('Question:', expression)
        answer = prompt.string('Your answer: ')
        if answer != correct_answer:
            print(GAME_OVER.format(answer, correct_answer))
            print("Let's try again, {0}!\n".format(name))
            break
        print('Correct!')
    else:
        print('Congratulations, {0}!\n'.format(name))