PATTERN_DIGIT_CHAR = 'd'
PATTERN_SEP_CHAR = 'p'
PATTERN_SEP_LIST = '-_.,:'
Y_RESULT = 'SI'
N_RESULT = 'NO'


def check_phone_number_by_pattern(phone_number, pattern):
    is_pattern_matched = True
    phone_number_len = len(phone_number)

    if phone_number_len != len(pattern):
        is_pattern_matched = False
    else:
        for i in range(phone_number_len):

            if pattern[i] == PATTERN_DIGIT_CHAR:
                if not phone_number[i].isdigit():
                    is_pattern_matched = False
                    break

            elif pattern[i] == PATTERN_SEP_CHAR:
                if phone_number[i] not in PATTERN_SEP_LIST:
                    is_pattern_matched = False
                    break

            elif pattern[i] != phone_number[i]:
                is_pattern_matched = False
                break

    return is_pattern_matched


def check_phone_number_by_pattern_list(phone_number, pattern_list):
    is_any_pattern_matched = N_RESULT

    for pattern in pattern_list:
        is_pattern_matched = check_phone_number_by_pattern(phone_number, pattern)

        if is_pattern_matched:
            is_any_pattern_matched = Y_RESULT
            break

    return is_any_pattern_matched


##################################################################################


PATTERN_LIST = ['7-ddd-ddd-dddd', '7-dddpddpdd', 'ddd-ddd-dddd', '+375-dd-ddd-dddd', 'X_1_dps']
VALID_MSG = "Phone number is VALID"
NOT_VALID_MSG = "Phone number is NOT VALID"


def main():
    phone_number = '7-000-111-2222'

    is_phone_valid = check_phone_number_by_pattern_list(phone_number, PATTERN_LIST) #or N_RESULT

    output = NOT_VALID_MSG
    if is_phone_valid == Y_RESULT:
        output = VALID_MSG

    print(output)


main()