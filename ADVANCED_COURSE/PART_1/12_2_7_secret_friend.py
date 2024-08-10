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
friend_list.reverse()
secret_friend_set_list = []
added_friend_list = []

for student in student_list:
    for friend in friend_list:
        if student != friend and friend not in added_friend_list:
            secret_friend_set_list.append(f'{student} - {friend}')
            added_friend_list.append(friend)
            break

print(*secret_friend_set_list, sep='\n')
# print(*added_friend_list, sep='\n')
