PUPIL_AMOUNT = 3

# pupil_marks_list = [set(input().split()) for _ in range(PUPIL_AMOUNT)]

pupil_marks_list = []

for _ in range(PUPIL_AMOUNT):
    pupil_marks = set(input())
    pupil_marks_list.append(pupil_marks)

common_marks = set()
# common marks except last pupil
for i in range(PUPIL_AMOUNT - 2):
    common_marks = pupil_marks_list[i] & pupil_marks_list[i + 1]

result_set = common_marks - pupil_marks_list[-1]

# pupil_marks_list = [set('4 2 5 10 6 2'.split()),
#                     set('10 4 7 6 3 10'.split()),
#                     set('1 2 1 5 9 5'.split())]
