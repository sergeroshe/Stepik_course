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


def main():
    num_value = int(input())
    print(is_prime(num_value))


main()
