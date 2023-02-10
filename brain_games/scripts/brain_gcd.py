#!/usr/bin/env python3
import prompt
import random


def main():
    print('Welcome to the Brain Games!')
    name = prompt.string('May I have your name? ')
    print("Hello, " + name)
    num_of_iter = 3
    print("Find the greatest common divisor of given numbers.")
    while num_of_iter:
        rand_num1 = random.randint(1, 100)
        rand_num2 = random.randint(1, 100)
        max_rand_num = max(rand_num1, rand_num2)
        min_rand_num = min(rand_num1, rand_num2)
        i = min_rand_num
        print(f'Question: {rand_num1} {rand_num2}')
        if max_rand_num % min_rand_num == 0:
            correct_answer = str(min_rand_num)
        if max_rand_num % min_rand_num != 0:
            while (rand_num1 % i != 0) or (rand_num2 % i != 0):
                i -= 1
            correct_answer = str(i)
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
