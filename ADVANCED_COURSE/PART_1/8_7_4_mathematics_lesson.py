PUPIL_AMOUNT = 3
MAX_COMMON_MARKS_PUPIL_AMOUNT = 2

# pupil_marks_set_list = [set(input().split()) for _ in range(PUPIL_AMOUNT)]
pupil_marks_set_list = [set('1 5 4 2 5 6 6 2 3 3 5 2'.split()),
                        set('2 3 5 10 2 10 2 6 7 10 10 6'.split()),
                        set('1 4 6 9 8 7 0 9 0 9 8 10'.split())]

all_pupils_unique_marks_set = set()

for pupil_marks_set in pupil_marks_set_list:
    all_pupils_unique_marks_set |= pupil_marks_set

all_pupils_common_mark_set = set()
result_mark_set = set()

# common marks calculation
for pupil_marks_set in pupil_marks_set_list:
    for mark in pupil_marks_set:
        mark_occurrence_amount = 0

        for marks_set in pupil_marks_set_list[1:]:
            if mark in marks_set:
                mark_occurrence_amount += 1
        # remove extra calc
        if mark_occurrence_amount <= MAX_COMMON_MARKS_PUPIL_AMOUNT:
            result_mark_set.add(mark)
        else:
            break
print(*sorted(result_mark_set, key=int))

# make test for different pupil amount e.g. 3/2

