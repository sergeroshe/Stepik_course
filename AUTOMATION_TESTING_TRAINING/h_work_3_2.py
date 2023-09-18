from typing import Tuple

# task 3 (optional)
# Винни-Пух посмотрел на свои цифровые часы: было 12:45.
# «Все цифры разные, самое время перекусить», — подумал он.
# Сколько раз за сутки Винни-Пуху можно перекусить?
# На цифровых часах Винни-Пуха отображаются четыре цифры — только часы и минуты.

HOURS_RANGE = 24
MINUTES_RANGE = 60


def get_two_dig_num(num):
    two_dig_num = str(num) if num > 9 else f'0{str(num)}'
    first_dig, second_dig = two_dig_num
    return first_dig, second_dig


def get_different_digits_amount() -> Tuple[int, list]:
    different_dig_count = 0
    snack_times_list = []

    for hour in range(HOURS_RANGE):
        hour_str = get_two_dig_num(hour)
        first_digit, second_digit = hour_str

        if first_digit == second_digit:
            continue
        for minute in range(MINUTES_RANGE):
            min_str = get_two_dig_num(minute)
            third_digit, fourth_digit = min_str

            if third_digit != fourth_digit and third_digit not in hour_str and fourth_digit not in hour_str:  # extract to var
                different_dig_count += 1
                snack_times_list.append(f'Винни-Пух посмотрел на свои цифровые часы - было {hour}:{minute}. '
                                        f'«Все цифры разные,'
                                        f' самое время перекусить!», — подумал он.')

    return different_dig_count, snack_times_list


def main():
    puhs_snacks_amount, snack_times_lst = get_different_digits_amount()
    print(*snack_times_lst, sep='\n')
    print()
    print(f'За сутки Винни-Пуху можно перекусить {puhs_snacks_amount} раза.')


main()
