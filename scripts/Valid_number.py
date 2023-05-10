POSITIVE_ANSWER = 'YES'
NEGATIVE_ANSWER = 'NO'
SEP_LIST = '.;:-,'
DIGIT_CHAR = 'd'
SEP_CHAR = 'p'
PATTERN_LIST = ['7-ddd-ddd-ddd4', '7-dddpddpdd', 'ddd-ddd-dddd', '+375-dd-ddd-dddd', 'X_1_dps']

phone_num = '7-111-111-1114' #  7-111-111-1111, 7-111.11;11, 111-111-1111, +375-25-640-8668, 7,111.11;11
phone_num_len = len(phone_num)

pattern_found = False # is pattern mathing number found in PATTERN_LIST

for pattern in PATTERN_LIST:
    pattern_matches = True
    if phone_num_len == len(pattern):
        for i in range(phone_num_len):
            if pattern[i] == DIGIT_CHAR:
                if not phone_num[i].isdigit():
                    pattern_matches = False
                    break
            elif pattern[i] == SEP_CHAR:
                if phone_num[i] not in SEP_LIST:
                    pattern_matches = False
                    break
            elif phone_num[i] != pattern[i]:
                pattern_matches = False
                break

    else:
        pattern_matches = False
        # continue

    if pattern_matches:
        pattern_found = True
        break


if pattern_found:
    print(POSITIVE_ANSWER)
else:
    print(NEGATIVE_ANSWER)
