questions = [
    {
        'question': 'Какой сегодня день?',
        'answers': {
            '0. Sreda',
            '1. Chetverg',
            '2. Pyatnitsa',
        },
        'correct_answer': 1
    }
]
correct_answer_cnt = 0
for question in questions:
    print(question('question'))
    for answer in question['answers']:
        print(answer)

    user_answer = int(input())
    
    if user_answer == question['corrent_answer']:
         correct_answer_cnt += 1
    if correct_answer_cnt/len(questions) < 0.7:
        print('You lost!')
    else:
        print('Congrats!')