from random import randint
from ..core import game_core


start_question = """Answer 'yes' if given number is prime.\
 Otherwise answer 'no'."""


def quiz():
    num = randint(2, 100)
    question = f'{num}'
    fst_psbl_dvsr = num // 2
    while num % fst_psbl_dvsr != 0:
        fst_psbl_dvsr -= 1
    if fst_psbl_dvsr == 1:
        correct_answer = 'yes'
    else:
        correct_answer = 'no'
    return question, correct_answer


def run_game():
    game_core(quiz, start_question)
