PUPIL_AMOUNT = 3
MAX_COMMON_MARKS_PUPIL_AMOUNT = 2

pupil_mark_set_list = [set(input().split()) for _ in range(PUPIL_AMOUNT)]

result_mark_set = set()
len_pupil_marks_set_list = len(pupil_mark_set_list)

for pupil_marks_set in pupil_mark_set_list:
    for mark in pupil_marks_set:
        mark_occurrence_amount = 0
        max_mark_occurrence_exceeded = False
        i = 0
        while not max_mark_occurrence_exceeded and i < len_pupil_marks_set_list:
            if mark in pupil_mark_set_list[i]:
                mark_occurrence_amount += 1
            max_mark_occurrence_exceeded = mark_occurrence_amount > MAX_COMMON_MARKS_PUPIL_AMOUNT
            i += 1

        if mark_occurrence_amount <= MAX_COMMON_MARKS_PUPIL_AMOUNT:
            result_mark_set.add(mark)
print(*sorted(result_mark_set, key=int))
