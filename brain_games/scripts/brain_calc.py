#!/usr/bin/env python3
import prompt
import random


def main():
    print('Welcome to the Brain Games!')
    name = prompt.string('May I have your name? ')
    print("Hello, " + name)
    num_of_iter = 3
    print("What is the result of the expression?")
    while num_of_iter:
        rand_num1 = random.randint(1, 25)
        rand_num2 = random.randint(1, 25)
        rand_oper = random.choice('+-*')
        print(f'Question: {rand_num1} {rand_oper} {rand_num2}')
        if rand_oper == '+':
            correct_answer = str(rand_num1 + rand_num2)
        if rand_oper == '-':
            correct_answer = str(rand_num1 - rand_num2)
        if rand_oper == '*':
            correct_answer = str(rand_num1 * rand_num2)
        user_answer = input('Your answer: ')
        if user_answer == correct_answer:
            print('Correct!')
        else:
            print(f"""'{user_answer}' is wrong answer ;(. \
Correct answer was '{correct_answer}'""")
            print(f'Let\'s try again, {name}')
            break
        num_of_iter -= 1
    if num_of_iter == 0:
        print(f'Congratulations, {name}!')


if __name__ == "__main__":
    main()
