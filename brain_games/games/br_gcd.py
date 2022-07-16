"""Module for the game brain-gcd."""

from math import gcd

from brain_games import games_logic as gml
from brain_games import generators as gen


def main_gcd() -> None:
    """Start the game brain-gcd."""
    gml.print_start_phrase()
    player_name = gml.meet_and_greet_player()
    print('Find the greatest common divisor of given numbers.')

    for (fst_num, snd_num) in gen.gen_gm_list(gen.gen_num_tuple):
        print('Question: ', fst_num, snd_num)

        is_player_wins = gml.compare_answers(
            str(gcd(fst_num, snd_num)),
            gml.get_player_answer(),
        )

        if is_player_wins:
            continue

        break

    gml.print_end_phrase(is_player_wins, player_name)


if __name__ == '__main__':
    main_gcd()
