PUPIL_AMOUNT = 3

pupil_marks_set_list = [set(input().split()) for _ in range(PUPIL_AMOUNT)]

all_pupils_unique_marks_set = set()

for pupil_marks_set in pupil_marks_set_list:
    all_pupils_unique_marks_set |= pupil_marks_set

all_pupils_common_mark_set = pupil_marks_set_list[0]

# common marks calculation
for pupil_marks_set in pupil_marks_set_list[1:]:
    all_pupils_common_mark_set &= pupil_marks_set

two_pupils_unique_marks_set = all_pupils_unique_marks_set - all_pupils_common_mark_set

print(*sorted(two_pupils_unique_marks_set, key=int))

# make test for different pupil amount e.g. 3/2

# pupil_marks_set_list = [set('1 5 4 2 5 6 6 2 3 3 5 2'.split()),
#                         set('2 3 5 10 2 10 2 6 7 10 10 6'.split()),
#                         set('1 4 6 9 8 7 0 9 0 9 8 10'.split())]