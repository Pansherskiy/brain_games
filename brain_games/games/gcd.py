from random import randint
from ..core import game_core


start_question = "Find the greatest common divisor of given numbers."


def quiz():
    rand_num1 = randint(1, 100)
    rand_num2 = randint(1, 100)
    max_rand_num = max(rand_num1, rand_num2)
    min_rand_num = min(rand_num1, rand_num2)
    i = min_rand_num
    question = f'{rand_num1} {rand_num2}'
    if max_rand_num % min_rand_num == 0:
        correct_answer = str(min_rand_num)
    if max_rand_num % min_rand_num != 0:
        while (rand_num1 % i != 0) or (rand_num2 % i != 0):
            i -= 1
        correct_answer = str(i)
    return question, correct_answer


def run_game():
    game_core(quiz, start_question)
