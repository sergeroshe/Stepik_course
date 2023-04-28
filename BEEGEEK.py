def is_valid_password(password): # reuse old functions
    pattern = 'a:b:c'.split(':')
    palindrome_char = 'a'
    prime_num_char = 'b'
    even_num_char = 'c'
    value = True
    for i in range(len(password)):
        password_num = password[i]
        password_len = len(password)
        if password_len == len(pattern):
            half_len = len(password_num) // 2
            if pattern[i] == palindrome_char:
                if password_num[:half_len] != password_num[half_len + len(password_num) % 2:][::-1]:
                    value = False
                    break
            elif pattern[i] == prime_num_char:
                for j in range(2, half_len + 2):
                    if int(password_num) % j == 0:
                        value = False
                        break
            elif pattern[i] == even_num_char:
                if int(password_num) % 2 != 0:
                    value = False
                    break
        else:
            value = False
            break
    return value


def main():
    user_password = input().split(':')
    print(is_valid_password(user_password))


main()