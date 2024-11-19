PUPIL_AMOUNT = 3
GROUP_ONE_PUPIL_AMOUNT = 2
GROUP_TWO_PUPIL_AMOUNT = PUPIL_AMOUNT - GROUP_ONE_PUPIL_AMOUNT

all_pupil_mark_set_list = [set(input().split()) for _ in range(PUPIL_AMOUNT)]

group_two_pupil_mark_set_list = all_pupil_mark_set_list[-GROUP_TWO_PUPIL_AMOUNT:]

group_one_pupil_mark_set = set()
for mark_set in all_pupil_mark_set_list[:-GROUP_TWO_PUPIL_AMOUNT]:
    group_one_pupil_mark_set |= mark_set

group_two_pupil_mark_set = set()
for mark_set in group_two_pupil_mark_set_list[-GROUP_TWO_PUPIL_AMOUNT:]:
    group_two_pupil_mark_set |= mark_set

group_two_unique_mark_set = group_two_pupil_mark_set - group_one_pupil_mark_set

print(*sorted(group_two_unique_mark_set, key=int, reverse=True))