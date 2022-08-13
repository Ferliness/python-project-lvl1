"""Module for the game brain-even."""

from brain_games import games_logic as gm_logic
from brain_games import games_math as gm_math
from brain_games import generators as gen


def main() -> None:
    """Start the game."""
    gm_logic.print_start_phrase()
    player_name = gm_logic.meet_and_greet_player()
    print('Answer "yes" if the number is even, otherwise answer "no".')
    answer_dict = {True: 'yes', False: 'no'}

    for num in gen.gen_gm_list(gen.gen_number):
        print('Question:', num)
        correct_answer = answer_dict[gm_math.is_even(num)]

        is_player_won = gm_logic.compare_answers(
            correct_answer,
            gm_logic.get_player_answer(),
        )

        if is_player_won:
            continue

        break

    gm_logic.print_end_phrase(is_player_won, player_name)


if __name__ == '__main__':
    main()
