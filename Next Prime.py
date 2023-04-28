def is_prime(num):
    answer = False
    count = 0
    for i in range(1, (num // 2) + 1):
        if num % i == 0:
            count += 1
        if count == 2:
            break
    count += 1
    if count == 2:
        answer = True

    return answer


def get_next_prime(next_num):
    next_num += 1
    next_prime_num = 0
    half_num = next_num // 2 + 1
    for i in range(next_num, next_num + half_num):
        if is_prime(i):
            next_prime_num = i
            break
    return next_prime_num


def main():
    num = int(input())
    greater_prime = get_next_prime(num)
    print(greater_prime)


main()

