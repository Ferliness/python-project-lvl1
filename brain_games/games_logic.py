"""Module contains the main logic of games."""


from brain_games import pu_service as pu_s
from brain_games import se_service as se_s

GAMES_COUNT = 3


def start_brain_even():
    """Start the game brain-even."""
    player_name = se_s.get_player_name()
    se_s.greet_player(player_name)
    print('Answer "yes" if the number is even, otherwise answer "no".')
    answer_dict = {True: 'yes', False: 'no'}

    for num in tuple(se_s.generate_number() for _ in range(GAMES_COUNT)):
        print('Question:', num)
        correct_answer = answer_dict[pu_s.is_even(num)]

        is_player_wins = se_s.compare_answers(
            correct_answer,
            se_s.get_player_answer(),
        )

        if is_player_wins:
            continue

        break

    se_s.print_end_phrases(is_player_wins, player_name)


if __name__ == '__main__':
    start_brain_even()
