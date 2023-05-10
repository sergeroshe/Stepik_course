import random

GREETING = 'Добро пожаловать в числовую угадайку'
START_RANGE = 1

print(GREETING)


def min_guaranteed_guess_count(start_range, end_range):
    middle = (start_range + end_range) // 2
    division_count = 0
    rand_num = random.randint(1, 100)

    while middle != start_range:
        middle = (start_range + end_range) // 2
        division_count += 1
        end_range = middle

    return division_count


def main():
    end_range = int(input())

    guaranteed_min_tries = min_guaranteed_guess_count(START_RANGE, end_range)

    print(guaranteed_min_tries)


def is_valid(input_string):
    result = input_string.isdigit() and 1 < int(input_string) < 100
    return result


input_value = input()
result_output = is_valid(input_value)
print(result_output)


# main()

