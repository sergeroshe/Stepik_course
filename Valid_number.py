POSITIVE_ANSWER = 'YES'
NEGATIVE_ANSWER = 'NO'
MATCH_LIST = '375.,:;-'
DIGIT_CHAR = 'd'
SEP_CHAR = 'p'
PATTERN_LIST = ['7-ddd-ddd-dddd', '7-dddpddpdd', 'ddd-ddd-dddd', '+375-dd-ddd-dddd']

phone_num = input() #  7-111-111-1111, 7-111.11;11, 111-111-1111, +375-25-640-8668, 7,111.11;11
phone_num_len = len(phone_num)

is_valid = True


for pattern in PATTERN_LIST:
    if phone_num_len != len(pattern):
        is_valid = False
        continue
    else:
        for i in range(phone_num_len):
            if pattern[i] in MATCH_LIST:
                if phone_num[i] != pattern[i]:
                    is_valid = False
                    break
            elif pattern[i] == DIGIT_CHAR:
                if not phone_num[i].isdigit():
                    is_valid = False
                    break
            elif pattern[i] == SEP_CHAR:
                if phone_num[i] not in MATCH_LIST:
                    is_valid = False
                    break
            is_valid = True
    if is_valid:
        break

if is_valid:
    print(POSITIVE_ANSWER)
else:
    print(NEGATIVE_ANSWER)


