"""Module for the game brain-even."""

from brain_games import games_logic as gm
from brain_games import generators as gen


def main_even():
    """Start the game brain-even."""
    gm.print_start_phrase()
    player_name = gm.meet_and_greet_player()
    print('Answer "yes" if the number is even, otherwise answer "no".')
    answer_dict = {True: 'yes', False: 'no'}

    for num in gen.gen_nums_list():
        print('Question:', num)
        correct_answer = answer_dict[_is_even(num)]

        is_player_wins = gm.compare_answers(
            correct_answer,
            gm.get_player_answer(),
        )

        if is_player_wins:
            continue

        break

    gm.print_end_phrase(is_player_wins, player_name)


def _is_even(number):
    """Сhecks if a number is even, return True/False.

    Args:
        number (int): The number to check

    Returns:
        return: bool
    """
    return number % 2 == 0


if __name__ == '__main__':
    main_even()
