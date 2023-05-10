START_RANGE = 1


def num_guessing_game(start_range, end_range):
    middle = (start_range + end_range) // 2
    division_count = 0

    while middle != start_range:
        middle = (start_range + end_range) // 2
        division_count += 1
        end_range = middle

    return division_count


def main():
    end_range = int(input())

    try_count = num_guessing_game(START_RANGE, end_range)

    print(try_count)


main()

