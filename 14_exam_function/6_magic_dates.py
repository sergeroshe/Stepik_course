SEPARATOR = '.'


def is_magic(date):
    date_part_list = date.split(SEPARATOR)
    result_output = int(date_part_list[0]) * int(date_part_list[1]) == int(date_part_list[2]) % 100

    return result_output


def main():
    date = input()

    is_date_magic = is_magic(date)

    print(is_date_magic)


main()