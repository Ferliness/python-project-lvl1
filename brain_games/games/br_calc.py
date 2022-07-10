"""Module for the game brain-calc."""

from brain_games import games_logic as gm
from brain_games import generators as gen


def main_calc():
    """Start the game brain-calc."""
    gm.print_start_phrase()
    player_name = gm.meet_and_greet_player()
    print('What is the result of the expression?')

    for (fst_num, snd_num) in gen.gen_tuples_list():
        math_opr = gen.gen_math_operator()
        print('Question: ', fst_num, math_opr, snd_num, sep='')

        is_player_wins = gm.compare_answers(
            str(_calc_expression(fst_num, snd_num, math_opr)),
            gm.get_player_answer(),
        )

        if is_player_wins:
            continue

        break

    gm.print_end_phrase(is_player_wins, player_name)


def _calc_expression(fst_number, snd_number, math_operator):
    """Calculate an expression and return the result, only '+', '-', '*'.

    Args:
        fst_number (int): first coefficent
        snd_number (int): second coefficent
        math_operator (string): type of operation

    Returns:
        int: expression result
    """
    if math_operator == '+':
        return fst_number + snd_number
    elif math_operator == '-':
        return fst_number - snd_number

    return fst_number * snd_number


if __name__ == '__main__':
    main_calc()
