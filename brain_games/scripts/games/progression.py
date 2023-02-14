from random import randint
from .core import game_core


start_question = "What number is missing in the progression?"


def quiz():
    progression = randint(1, 15)
    fst_num_in_lst = randint(1, 100)
    last_num_in_lst = fst_num_in_lst + progression * 10
    lst = list(range(fst_num_in_lst, last_num_in_lst, progression))
    index = randint(0, 9)
    correct_answer = str(lst[index])
    lst[index] = '..'
    question = ' '.join(str(i) for i in lst)
    return question, correct_answer


def run_game():
    game_core(quiz, start_question)
