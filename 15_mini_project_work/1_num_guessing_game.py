START_RANGE = 1


def min_guaranteed_guess_count(start_range, end_range):
    middle = (start_range + end_range) // 2
    division_count = 0

    while middle != start_range:
        middle = (start_range + end_range) // 2
        division_count += 1
        end_range = middle

    return division_count


def main():
    end_range = int(input())

    guaranteed_min_tries = min_guaranteed_guess_count(START_RANGE, end_range)

    print(guaranteed_min_tries)


main()

