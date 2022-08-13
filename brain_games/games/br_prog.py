"""Module for the game brain-prog."""

from typing import List

from brain_games import games_logic as gm_logic
from brain_games import generators as gen


def main() -> None:
    """Start the game."""
    gm_logic.print_start_phrase()
    player_name = gm_logic.meet_and_greet_player()
    print('What number is missing in the progression?')

    for prog in gen.gen_gm_list(gen.gen_prog):
        index_hidden_elem = gen.gen_number(gen.MIN_NUM, gen.REC_LEN_LIST)
        print('Question:', ' '.join(make_hidden_prog(prog, index_hidden_elem)))

        is_player_wins = gm_logic.compare_answers(
            str(prog[index_hidden_elem]),
            gm_logic.get_player_answer(),
        )

        if is_player_wins:
            continue

        break

    gm_logic.print_end_phrase(is_player_wins, player_name)


def make_hidden_prog(prog: List[int], index_hidden_elem: int) -> List[str]:
    """Hide progression element whose index is equal to index_hidden_elem.

    index_hidden_elem must be less than length of the progression.

    Args:
        prog (List[int]): some progression
        index_hidden_elem (int): the index of the element to hide

    Returns:
        List[str]: list of strings based on progression
        without one element
    """
    return [
        '..' if count == index_hidden_elem else str(num)
        for count, num in enumerate(prog)
    ]


if __name__ == '__main__':
    main()
