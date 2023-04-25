def is_password_good(password):
    value = False
    has_lower = False
    has_upper = False
    has_digit = False
    min_len = 8
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
    print(is_password_good(user_password))


main()
