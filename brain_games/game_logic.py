"""Module contains the main logic of the game."""

from random import randint

import prompt

MIN_NUM, MAX_NUM, LEN_LIST = 0, 1000, 3


def brain_even():
    """Start the game."""
    print('Welcome to the Brain Games!')
    player_name = prompt.string(prompt='May I have your name? ')
    print('Hello,', player_name)
    print('Answer "yes" if the number is even, otherwise answer "no".')

    is_player_wins = True

    for num in tuple(randint(MIN_NUM, MAX_NUM) for _ in range(LEN_LIST)):
        print('Question:', num)
        player_answer = prompt.string(prompt='Your answer: ')
        correct_answer = get_answer_even_or_odd(num)

        if player_answer == correct_answer:
            print('Correct!')
        else:
            print(
                "'",
                player_answer,
                "' is wrong answer ;(. Correct answer was '",
                correct_answer,
                "'",
                sep='',
            )
            is_player_wins = False
            break

    if is_player_wins:
        print('Congratulations,', player_name)
    else:
        print("Let's try again,", player_name)


def get_answer_even_or_odd(number):
    """Check the number for game, return "yes"/"no".

    Args:
        number (int): The number to check

    Returns:
        return: string
    """
    answer_dict = {True: 'yes', False: 'no'}
    return answer_dict[is_even(number)]


def is_even(number):
    """Сhecks if a number is even, return True/False.

    Args:
        number (int): The number to check

    Returns:
        return: bool
    """
    return number % 2 == 0


if __name__ == '__main__':
    brain_even()
