POSITIVE_ANSWER = 'YES'
NEGATIVE_ANSWER = 'NO'

num_string_list = input().split()
# num_string_list = '10 5 48 6 38 1'.split()
num_string_list = [el.lstrip('0') for el in num_string_list]

non_repeated_num_set = set()
answer_list = []

for num in num_string_list:
    if num not in non_repeated_num_set:
        answer_list.append(NEGATIVE_ANSWER)
        non_repeated_num_set.add(num)
    else:
        answer_list.append(POSITIVE_ANSWER)

print(*answer_list, sep='\n')
