"""Module for the game brain-even."""

from brain_games import games_logic as gml
from brain_games import generators as gen


def main_even() -> None:
    """Start the game brain-even."""
    gml.print_start_phrase()
    player_name = gml.meet_and_greet_player()
    print('Answer "yes" if the number is even, otherwise answer "no".')
    answer_dict = {True: 'yes', False: 'no'}

    for num in gen.gen_gm_list(gen.gen_number):
        print('Question:', num)
        correct_answer = answer_dict[_is_even(num)]

        is_player_wins = gml.compare_answers(
            correct_answer,
            gml.get_player_answer(),
        )

        if is_player_wins:
            continue

        break

    gml.print_end_phrase(is_player_wins, player_name)


def _is_even(number: int) -> bool:
    """Сhecks if a number is even, return True/False.

    Args:
        number (int): the number to check

    Returns:
        bool: the result of checking
    """
    return number % 2 == 0


if __name__ == '__main__':
    main_even()
