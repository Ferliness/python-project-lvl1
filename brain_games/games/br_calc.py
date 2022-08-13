"""Module for the game brain-calc."""

from brain_games import games_logic as gm_logic
from brain_games import games_math as gm_math
from brain_games import generators as gen


def main() -> None:
    """Start the game."""
    gm_logic.print_start_phrase()
    player_name = gm_logic.meet_and_greet_player()
    print('What is the result of the expression?')

    for (fst_num, snd_num) in gen.gen_gm_list(gen.gen_num_tuple):
        math_opr = gen.gen_math_operator()
        print('Question:', fst_num, math_opr, snd_num)

        is_player_wins = gm_logic.compare_answers(
            str(gm_math.calc_expression(fst_num, snd_num, math_opr)),
            gm_logic.get_player_answer(),
        )

        if is_player_wins:
            continue

        break

    gm_logic.print_end_phrase(is_player_wins, player_name)


if __name__ == '__main__':
    main()
