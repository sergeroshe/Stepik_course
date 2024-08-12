from random import choice

student_amount = 5
# student_amount = int(input())
# student_list = [input() for _ in range(student_amount)]
student_list = ['Владимир Смолов',
                'Тагир Хан',
                'Давид Лавров',
                'Арина Приходько',
                'Глеб Анисимов']

friend_list = student_list.copy()
secret_friend_set_list = []
added_friend_list = []

for student in student_list:
    if student in friend_list:
        friend_list.remove(student)
    friend_found = False
    while not friend_found:
        friend = choice(friend_list)
        if friend not in added_friend_list:
            added_friend_list.append(friend)
            secret_friend_set_list.append(f'{student} - {friend}')
            friend_found = True
            friend_list.remove(friend)

    friend_list.append(student)


print(*secret_friend_set_list, sep='\n')


# student_list = ['Владимир Смолов',
#                 'Тагир Хан',
#                 'Давид Лавров',
#                 'Арина Приходько',
#                 'Глеб Анисимов']
