POSITIVE = 'YES'
NEGATIVE = 'NO'
SEP_LIST = '. , : ; -'
DIGIT_CHAR = 'd'
SEP_CHAR = 'p'

# PATTERN = '7-dddpddpdd'
PATTERN_LIST = ['7-dddpddpdd', '7-ddd-ddd-dddd', 'ddd-ddd-dddd', '+375-dd-ddd-dddd']
pattern_1_len = len(PATTERN_LIST[0])
pattern_2_len = len(PATTERN_LIST[1])
pattern_3_len = len(PATTERN_LIST[2])
pattern_4_len = len(PATTERN_LIST[3])


phone_num = '7-123-111-1111'
phone_num_len = len(phone_num)

output = POSITIVE

# if phone_num_len == pattern_1_len:
for pattern in PATTERN_LIST:
    if phone_num_len == len(pattern):
    for i in range(phone_num_len):
        elif PATTERN_LIST[1][i] == DIGIT_CHAR:
            #  process d
            if not phone_num[i].isdigit():
                output = NEGATIVE
                break
#         elif PATTERN_LIST[0][i] == SEP_CHAR:
#             if phone_num[i] not in SEP_LIST:
#                 output = NEGATIVE
#                 break
#         else:
#             if phone_num[i] != PATTERN_LIST[0][i]:
#                 output = NEGATIVE
#                 break
#
# elif phone_num_len == pattern_2_len:
#     for i in range(phone_num_len):
#         if PATTERN_LIST[1][i] == DIGIT_CHAR:
#             if not phone_num[i].isdigit():
#                 output = NEGATIVE
#                 break
#             if phone_num[i] != PATTERN_LIST[1][i]:
#                 output = NEGATIVE
#                 break
#
# elif phone_num_len == pattern_3_len:
#     for i in range(phone_num_len):
#         if PATTERN_LIST[2][i] == DIGIT_CHAR:
#             if not phone_num[i].isdigit():
#                 output = NEGATIVE
#                 break
#             if phone_num[i] != PATTERN_LIST[2][i]:
#                 output = NEGATIVE
#                 break
#
# elif phone_num_len == pattern_4_len:
#     for i in range(phone_num_len):
#         if PATTERN_LIST[3][i] == DIGIT_CHAR:
#             if not phone_num[i].isdigit():
#                 output = NEGATIVE
#                 break
#             if phone_num[i] != PATTERN_LIST[3][i]:
#                 output = NEGATIVE
#                 break

# else:
#     output = NEGATIVE


print(output)


