def get_days(month_num):
    month_day_number_list = [31, 30, 28]
    long_months_idx_list = [1, 3, 5, 7, 8, 10, 12]
    medium_months_idx_list = [4, 6, 9, 11]
    result = 0

    if month_num in long_months_idx_list:
        result = month_day_number_list[0]
    elif month_num in medium_months_idx_list:
        result = month_day_number_list[1]
    else:
        result = month_day_number_list[2]

    return result


def main():
    month_number = int(input())
    print(get_days(month_number))


main()