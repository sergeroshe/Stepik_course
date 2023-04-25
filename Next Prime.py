def is_prime(num):
    next_prime_num = 0
    next_num = num + 1
    half_num = next_num // 2 + 1
    for i in range(next_num, next_num + half_num):
        count = 0
        for j in range(1, half_num):
            if i % j == 0:
                count += 1
            if count == 2:
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
