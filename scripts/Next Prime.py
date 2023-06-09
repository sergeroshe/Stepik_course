def is_prime(num):
    answer = True
    if num > 1:
        for i in range(2, (num // 2) + 1):
            if num % i == 0:
                answer = False
                break
    else:
        answer = False
    return answer


def get_next_prime(next_num):
    next_prime_num = next_num + 1
    while not is_prime(next_prime_num):  # until found
        next_prime_num += 1
    return next_prime_num


def main():

    num = int(input())

    greater_prime = get_next_prime(num)

    print(greater_prime)


main()

