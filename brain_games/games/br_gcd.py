"""Module for the game brain-gcd."""

from math import gcd

from brain_games import games_logic as gm
from brain_games import generators as gen


def main_gcd() -> None:
    """Start the game brain-gcd."""
    gm.print_start_phrase()
    player_name = gm.meet_and_greet_player()
    print('Find the greatest common divisor of given numbers.')

    for (fst_num, snd_num) in gen.gen_tuples_list():
        print('Question: ', fst_num, snd_num)

        is_player_wins = gm.compare_answers(
            str(gcd(fst_num, snd_num)),
            gm.get_player_answer(),
        )

        if is_player_wins:
            continue

        break

    gm.print_end_phrase(is_player_wins, player_name)


if __name__ == '__main__':
    main_gcd()
