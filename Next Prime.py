def is_prime(num):
    count = 0
    next_prime_num = 0
    for i in range(num + 1, (num + 1) + (num // 2 + 1)):
        count = 0
        for j in range(1, ((num + 1) // 2) + 1):
            if i % j == 0:
                count += 1
            if count > 2:
                break
        count += 1
        if count == 2:
            next_prime_num = i
            break
    return next_prime_num


def main():
    num_value = int(input())
    print(is_prime(num_value))


main()