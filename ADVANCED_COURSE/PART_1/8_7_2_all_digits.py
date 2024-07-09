POSITIVE_ANSWER = 'YES'
NEGATIVE_ANSWER = 'NO'

num_one = set(input())
num_two = set(input())

answer = POSITIVE_ANSWER

have_all_digits = num_two.issubset(num_one)

if not have_all_digits:
    answer = NEGATIVE_ANSWER

print(answer)


# num_one = set('1254')
# num_two = set('1243')
# num_one = set('123456789')
# num_two = set('657')