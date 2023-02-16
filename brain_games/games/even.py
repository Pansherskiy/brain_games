from random import randint
from ..core import game_core


start_question = """Answer "yes" if the number is even,\
 otherwise answer "no"."""


def quiz():
    question = randint(1, 100)
    correct_answer = 'yes' if question % 2 == 0 else 'no'
    return question, correct_answer


def run_game():
    game_core(quiz, start_question)
