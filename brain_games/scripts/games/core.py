import prompt


def game_core(quiz, start_question):
    num_of_iter = 3
    print('Welcome to the Brain Games!')
    name = prompt.string('May I have your name? ')
    print("Hello, " + name)
    print(start_question)
    while num_of_iter:
        generated_question, correct_answer = quiz()
        print(f'Question: {generated_question}')
        user_answer = input('Your answer: ')
        if user_answer == correct_answer:
            print('Correct!')
            num_of_iter -= 1
        else:
            print(f"""'{user_answer}' is wrong answer ;(. \
Correct answer was '{correct_answer}'""")
            print(f'Let\'s try again, {name}')
            break
    if num_of_iter == 0:
        print(f'Congratulations, {name}!')
