#!/usr/bin/env python3
import prompt
import random


def main():
    print('Welcome to the Brain Games!')
    name = prompt.string('May I have your name? ')
    print("Hello, " + name)
    num_of_iter = 3
    print("Answer 'yes' if number even otherwise answer 'no'.")
    while num_of_iter:
        random_number = random.randint(1, 100)
        print(f'Question: {random_number}')
        user_answer = input('Your answer: ')
        correct_answer = 'yes' if random_number % 2 == 0 else 'no'
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
