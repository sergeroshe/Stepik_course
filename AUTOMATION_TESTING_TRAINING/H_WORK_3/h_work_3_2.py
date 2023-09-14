# task 3 (optional)
# Винни-Пух посмотрел на свои цифровые часы: было 12:45.
# «Все цифры разные, самое время перекусить», — подумал он.
# Сколько раз за сутки Винни-Пуху можно перекусить?
# На цифровых часах Винни-Пуха отображаются четыре цифры — только часы и минуты.

HOURS_RANGE = 24
MINUTES_RANGE = 60


def get_different_digits_amount(hours_range, minutes_range):
    different_dig_count = 0
    snack_times_list = []

    for h in range(hours_range):
        h = str(h)
        if int(h) < 10:
            h = str(0) + h
        if h[0] != h[1]:
            for m in range(minutes_range):
                m = str(m)
                if int(m) < 10:
                    m = str(0) + m
                if m[0] != m[1] and m[0] not in h and m[1] not in h:
                    different_dig_count += 1
                    snack_times_list.append(f'Винни-Пух посмотрел на свои цифровые часы - было {h}:{m}. '
                                            f'«Все цифры разные,'
                                            f' самое время перекусить!», — подумал он.')

    return different_dig_count, snack_times_list


def main():
    puhs_snacks_amount, snack_times_lst = get_different_digits_amount(HOURS_RANGE, MINUTES_RANGE)
    print(*snack_times_lst, sep='\n')
    print()
    print(f'За сутки Винни-Пуху можно перекусить {puhs_snacks_amount} раза.')


main()

