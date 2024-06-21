POSITIVE_ANSWER = 'YES'
NEGATIVE_ANSWER = 'NO'

num_string_list = input().split()
# string_list = '1 2 3 002 03 4 5 05'.split()
num_string_list = [el.lstrip('0') for el in num_string_list]

non_repeated_num_set = set()
answer_list = []

for num in num_string_list:
    if num not in non_repeated_num_set:
        non_repeated_num_set.add(num)
        answer_list.append(NEGATIVE_ANSWER)
    else:
        answer_list.append(POSITIVE_ANSWER)

print(*answer_list, sep='\n')
