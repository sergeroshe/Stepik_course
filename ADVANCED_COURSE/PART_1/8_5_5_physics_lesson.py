PUPIL_AMOUNT = 3

pupil_marks_set_list = [set(input().split()) for _ in range(PUPIL_AMOUNT)]

all_pupils_unique_marks_set = set()

for pupil_marks_set in pupil_marks_set_list:
    all_pupils_unique_marks_set |= pupil_marks_set

third_pupil_unique_marks_set = pupil_marks_set_list[2] - \
                               pupil_marks_set_list[0] - \
                               pupil_marks_set_list[1]

print(*sorted(third_pupil_unique_marks_set, key=int, reverse=True))

# pupil_marks_set_list = [set('1 5 4 2 5 6 6 2 3 3 5 2'.split()),
#                         set('2 3 5 1 2 1 2 6 7 1 1 6'.split()),
#                         set('1 4 6 9 8 7 0 9 0 9 8 10'.split())]