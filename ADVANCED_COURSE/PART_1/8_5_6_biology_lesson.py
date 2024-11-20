PUPIL_AMOUNT = 3
DIGIT_AMOUNT = 10

all_digit_set = set()

for i in range(DIGIT_AMOUNT + 1):
    all_digit_set.add(str(i))

pupil_marks_set_list = [set(input().split()) for _ in range(PUPIL_AMOUNT)]

two_pupils_unique_marks_set = all_digit_set - pupil_marks_set_list[0] - pupil_marks_set_list[1]\
                              - pupil_marks_set_list[2]

print(*sorted(two_pupils_unique_marks_set, key=int))
#
# pupil_marks_set_list = [set('1 5 4 2 5 6 6 2 3 3 5 2'.split()),
#                         set('2 3 5 1 2 1 2 6 7 1 1 6'.split()),
#                         set('1 4 6 8 8 7 0 6 0 3 8 1'.split())]