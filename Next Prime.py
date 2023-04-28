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
    next_num += 1
    i = next_num
    while not is_prime(i):  # until found
        i += 1
    next_prime_num = i
    return next_prime_num


def main():
    num = int(input())
    greater_prime = get_next_prime(num)
    print(greater_prime)


main()

