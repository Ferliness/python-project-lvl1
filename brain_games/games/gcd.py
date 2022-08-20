"""Module for the game brain-gcd."""

from math import gcd

from brain_games import games_logic as gm_logic
from brain_games import generators as gen


def main() -> None:
    """Start the game."""
    gm_logic.print_start_phrase()
    player_name = gm_logic.meet_and_greet_player()
    print('Find the greatest common divisor of given numbers.')

    for (fst_num, snd_num) in gen.gen_gm_list(gen.gen_num_tuple):
        print('Question:', fst_num, snd_num)

        is_player_won = gm_logic.compare_answers(
            str(gcd(fst_num, snd_num)),
            gm_logic.get_player_answer(),
        )

        if is_player_won:
            continue

        break

    gm_logic.print_end_phrase(is_player_won, player_name)
