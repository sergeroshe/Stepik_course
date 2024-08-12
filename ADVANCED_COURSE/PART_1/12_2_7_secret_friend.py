from random import shuffle

student_amount = int(input())
student_list = [input() for _ in range(student_amount)]

friend_list = student_list.copy()
shuffle(friend_list)
secret_friend_set_list = []
added_friend_list = []

for student in student_list:
    friend_list.remove(student)
    friend_found = False

    i = 0
    while i < len(friend_list) and not friend_found:
        friend = friend_list[i]
        if friend not in added_friend_list:
            added_friend_list.append(friend)
            secret_friend_set_list.append(f'{student} - {friend}')
            friend_found = True
        else:
            i += 1
    friend_list.append(student)


print(*secret_friend_set_list, sep='\n')


# student_list = ['Владимир Смолов',
#                 'Тагир Хан',
#                 'Давид Лавров',
#                 'Арина Приходько',
#                 'Глеб Анисимов']
