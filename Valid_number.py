POSITIVE = 'YES'
NEGATIVE = 'NO'
SEP_LIST = '. , : ; -'
DIGIT_CHAR = 'd'
SEP_CHAR = 'p'
PATTERN_LIST = ['7-ddd-ddd-dddd', '7-dddpddpdd', 'ddd-ddd-dddd', '+375-dd-ddd-dddd']

phone_num = input() #  7-111-111-1111, 7-111.11;11, 111-111-1111, +375-25-640-8668
phone_num_len = len(phone_num)

output = POSITIVE

for pattern in PATTERN_LIST:
    if phone_num_len != len(pattern):
        output = NEGATIVE
        continue
    else:
        for i in range(phone_num_len):
            if pattern[i].isdigit() or pattern[i] in SEP_LIST:
                if phone_num[i] != pattern[i]:
                    output = NEGATIVE
                    break
            elif pattern[i] == DIGIT_CHAR:
                if not phone_num[i].isdigit():
                    output = NEGATIVE
                    break
            elif pattern[i] == SEP_CHAR:
                if phone_num[i] not in SEP_LIST:
                    output = NEGATIVE
                    break
            output = POSITIVE
    if output == POSITIVE:
        break

print(output)
