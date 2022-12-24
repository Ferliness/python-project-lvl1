"""The module contains the main engine for brain games."""

from types import ModuleType

import prompt

GAMES_COUNT = 3


def run_game(game: ModuleType) -> None:
    """Start the game.

    Args:
        game (ModuleType): one of the brain games
    """
    print('Welcome to the Brain Games!')
    player_name = prompt.string(prompt='May I have your name? ')
    print(f'Hello, {player_name}!')
    print(game.DESCRIPTION)

    is_player_won = True
    for _ in range(GAMES_COUNT):
        question, answer = game.get_question_and_answer()
        print(f'Question: {question}')

        player_answer = prompt.string(prompt='Your answer: ')

        if answer == player_answer:
            print('Correct!')
        else:
            is_player_won = False
            print(
                f"'{player_answer}' is wrong answer ;(.",
                f"Correct answer was '{answer}'.",
            )
            break

    if is_player_won:
        print('Congratulations, ', player_name, '!', sep='')
    else:
        print("Let's try again, ", player_name, '!', sep='')
