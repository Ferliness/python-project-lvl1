"""Module for the game brain-calc."""

from brain_games import games_logic as gml
from brain_games import generators as gen


def main() -> None:
    """Start the game brain-calc."""
    gml.print_start_phrase()
    player_name = gml.meet_and_greet_player()
    print('What is the result of the expression?')

    for (fst_num, snd_num) in gen.gen_gm_list(gen.gen_num_tuple):
        math_opr = gen.gen_math_operator()
        print('Question: ', fst_num, math_opr, snd_num, sep='')

        is_player_wins = gml.compare_answers(
            str(_calc_expression(fst_num, snd_num, math_opr)),
            gml.get_player_answer(),
        )

        if is_player_wins:
            continue

        break

    gml.print_end_phrase(is_player_wins, player_name)


def _calc_expression(
    fst_number: int,
    snd_number: int,
    math_operator: str,
) -> int:
    """Calculate an expression and return the result, only '+', '-', '*'.

    Args:
        fst_number (int): first coefficent
        snd_number (int): second coefficent
        math_operator (str): type of operation

    Returns:
        int: expression result
    """
    if math_operator == '+':
        return fst_number + snd_number
    elif math_operator == '-':
        return fst_number - snd_number

    return fst_number * snd_number


if __name__ == '__main__':
    main()
