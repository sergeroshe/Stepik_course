Y_ANSWER = 'YES'
N_ANSWER = 'NO'
DIG_AMOUNT = 10

answer = N_ANSWER

digit_combined_string_list = [int(el) for el in (input() + input())]

if len(set(digit_combined_string_list)) == DIG_AMOUNT:
    answer = Y_ANSWER

print(answer)
