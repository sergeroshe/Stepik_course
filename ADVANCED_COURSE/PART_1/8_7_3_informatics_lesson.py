PUPIL_AMOUNT = 3

pupil_marks_list = [set(input().split()) for _ in range(PUPIL_AMOUNT)]

third_pupil_unique_marks = (pupil_marks_list[0] & pupil_marks_list[1]) - pupil_marks_list[2]

print(*sorted(third_pupil_unique_marks, reverse=False, key=int))
#
# pupil_marks_list = [set('4 2 5 10 6 2'.split()),
#                     set('10 4 7 6 3 10'.split()),
#                     set('1 2 1 5 9 5'.split())]