PUPIL_AMOUNT = 3
MAX_COMMON_MARKS_PUPIL_AMOUNT = 2

pupil_marks_set_list = [set(input().split()) for _ in range(PUPIL_AMOUNT)]


all_pupils_unique_marks_set = set()

for pupil_marks_set in pupil_marks_set_list:
    all_pupils_unique_marks_set |= pupil_marks_set

all_pupils_common_mark_set = set()
result_mark_set = set()

# common marks calculation
for pupil_marks_set in pupil_marks_set_list:
    for mark in pupil_marks_set:
        mark_occurrience_amount = 0

        for marks_set in pupil_marks_set_list:
            if mark in marks_set:
                mark_occurrience_amount += 1
            if mark_occurrience_amount > MAX_COMMON_MARKS_PUPIL_AMOUNT:
                break
        if mark_occurrience_amount <= MAX_COMMON_MARKS_PUPIL_AMOUNT:
            result_mark_set.add(mark)
print(*sorted(result_mark_set, key=int))