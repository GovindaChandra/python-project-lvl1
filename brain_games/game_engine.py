"""Global settings for games."""

import prompt

NUMBER_OF_ROUNDS = 3
GAME_OVER = "'{0}' is wrong answer ;(. Correct answer was '{1}'."


def start_game(game):
    """Print greeting, lunch game function.

    Parameters:
        game: Contain game rules, game logic, data generation function
    """
    print('\nWelcome to the Brain Games!')
    name = prompt.string('May I have your name? ')
    print('Hello, {0}!\n'.format(name))
    print(game.GAME_RULE)
    for _ in range(NUMBER_OF_ROUNDS):
        expression, correct_answer = game.game_data_function()
        print('Question:', expression)
        answer = prompt.string('Your answer: ')
        if answer != correct_answer:
            print(GAME_OVER.format(answer, correct_answer))
            print("Let's try again, {0}!\n".format(name))
            break
        print('Correct!')
    else:
        print('Congratulations, {0}!\n'.format(name))
