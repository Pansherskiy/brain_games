from random import randint, choice
from .core import game_core


start_question = "What is the result of the expression?"


def quiz():
    rand_num1 = randint(1, 25)
    rand_num2 = randint(1, 25)
    rand_oper = choice('+-*')
    question = f'{rand_num1} {rand_oper} {rand_num2}'
    if rand_oper == '+':
        correct_answer = str(rand_num1 + rand_num2)
    if rand_oper == '-':
        correct_answer = str(rand_num1 - rand_num2)
    if rand_oper == '*':
        correct_answer = str(rand_num1 * rand_num2)
    return question, correct_answer


def run_game():
    game_core(quiz, start_question)
