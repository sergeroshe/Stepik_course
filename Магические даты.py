# объявление функции
def is_magic(date):
    result_output = False
    if int(date_part_list[0]) * int(date_part_list[1]) == int(date_part_list[2]) % 100:
        result_output = True

    return result_output


date = input()
date_part_list = date.split('.')


print(is_magic(date_part_list))