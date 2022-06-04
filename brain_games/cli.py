"""Module containing logic."""
import prompt


def welcome_user():
    """Player greeting."""
    print('Welcome to the Brain Games!')
    user_name = prompt.string(prompt='May I have your name? ')
    print('Hello,', user_name)


if __name__ == '__main__':
    welcome_user()
