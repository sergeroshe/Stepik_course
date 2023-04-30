MIN_LEN = 8


def is_password_good(password, min_len):
    value = False
    has_lower = False
    has_upper = False
    has_digit = False
    pass_len = len(password)

    if pass_len >= min_len:
        for char in password:
            if char.islower():
                has_lower = True
            elif char.isupper():
                has_upper = True
            elif char.isdigit():
                has_digit = True
        if has_lower and has_upper and has_digit:
            value = True
    else:
        value = False

    return value


def main():
    user_password = input()

    is_passwd_valid = is_password_good(user_password, MIN_LEN)

    print(is_passwd_valid)


main()
