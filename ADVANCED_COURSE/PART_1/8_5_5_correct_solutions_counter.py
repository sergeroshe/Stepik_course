CORRECT_ANSWER = 'Correct'
NO_CORRECT_SOLUTIONS_ANSWER = 'Вы можете стать первым, кто решит эту задачу'
INACCURACY_MEASURE = 0.001

attempts_total_amount = int(input())

result_list = [input() for _ in range(attempts_total_amount)]

len_result_list = len(result_list)

correct_answer_counter = 0
unique_correct_answer_set = set()
for result in result_list:
    if result.split()[-1] == CORRECT_ANSWER:
        correct_answer_counter += 1
        unique_correct_answer_set.add(result)

unique_correct_answer_counter = len(unique_correct_answer_set)

if unique_correct_answer_counter:
    correct_answer_percentage = round(correct_answer_counter / len_result_list * 100 + INACCURACY_MEASURE)
    print(f'Верно решили {unique_correct_answer_counter} учащихся\n'
          f'Из всех попыток {correct_answer_percentage}% верных')
else:
    print(NO_CORRECT_SOLUTIONS_ANSWER)

# result_list = ['Поколение Python: Correct', 'Вася Пупкин: Wrong', 'evil_666: Correct', 'Поколение Python: Correct',
#                'Поколение Python: Wrong', 'Сэм Альтман: Correct']

