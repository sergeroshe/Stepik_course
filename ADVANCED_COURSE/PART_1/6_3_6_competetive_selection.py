pupil_amount = int(input())

pupil_list = []
for i in range(pupil_amount):
    pupil_info = input().split()
    pupil = (pupil_info[0], int(pupil_info[-1]))
    pupil_list.append(pupil)


result_list = []
all_pupil_list = [pupil for pupil in pupil_list]
result_list.append(all_pupil_list)

excellent_student_list = [ex_pupil for ex_pupil in pupil_list if ex_pupil[-1] > 3]
result_list.append(excellent_student_list)

for pupil_info_list in result_list:
    for pupil_info in pupil_info_list:
        print(*pupil_info)
    print()

# pupil_list = ['Круглов 4'.split(),
#               'Кузнецов 5'.split(),
#               'Федин 4'.split(),
#               'Тарасов 2'.split(),
#               'Словецкий 3'.split()]
# pupil_list = ['Круглов 4',
#               'Кузнецов 5',
#               'Федин 4',
#               'Тарасов 2',
#               'Словецкий 3']
