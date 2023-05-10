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


def main():
    num_value = int(input())
    is_number_prime = is_prime(num_value)
    print(is_number_prime)


main()
