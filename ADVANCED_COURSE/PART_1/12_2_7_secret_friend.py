# student_amount = int(input())
from random import shuffle

student_amount = 5

# student_list = [input() for _ in range(student_amount)]
student_list = ['Владимир Смолов',
                'Тагир Хан',
                'Давид Лавров',
                'Арина Приходько',
                'Глеб Анисимов']
friend_list = student_list.copy()
shuffle(friend_list)
secret_friend_set_list = []
added_friend_list = []

for student in student_list:
    friend_list.remove(student)
    for friend in friend_list:
        if friend not in added_friend_list:
            secret_friend_set_list.append(f'{student} - {friend}')
            added_friend_list.append(friend)
            break
    friend_list.append(student)

print(*secret_friend_set_list, sep='\n')
# print(*added_friend_list, sep='\n')
