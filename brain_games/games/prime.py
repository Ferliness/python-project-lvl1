"""The module for the game brain-prime."""

from math import sqrt
from random import randint

DESCRIPTION = 'Answer "yes" if given number is prime. Otherwise answer "no".'
MIN_NUM, MAX_NUM = 0, 100


def get_question_and_answer() -> tuple[str, str]:
    """Generate and give a game question and answer to it.

    Returns:
        tuple[str, str]: (question, answer)
    """
    answer_dict = {True: 'yes', False: 'no'}
    number = randint(MIN_NUM, MAX_NUM)

    question = f'Question: {number}'
    answer = answer_dict[is_prime(number)]

    return question, answer


def is_even(number: int) -> bool:
    """Сheck if a number is even.

    Args:
        number (int): the number to check

    Returns:
        bool: the result of checking
    """
    return number % 2 == 0


def is_remainder(divisor: int, number: int) -> bool:
    """Check if there is a remainder after dividing the number by the divisor.

    Args:
        divisor (int): divisor of the passed number
        number (int): number to be divided

    Returns:
        bool: the result of checking
    """
    no_remainder = 0
    return number % divisor != no_remainder


def is_prime(number: int) -> bool:
    """Check if a number is prime. Only for numbers greater than zero.

    Args:
        number (int): the number to check

    Returns:
        bool: the result of checking
    """
    min_even_prime = 2
    if is_even(number) or min_even_prime > number:
        return number == min_even_prime

    odd_divisor = 3
    while odd_divisor <= sqrt(number) and is_remainder(odd_divisor, number):
        odd_divisor += min_even_prime
    return odd_divisor > sqrt(number)
