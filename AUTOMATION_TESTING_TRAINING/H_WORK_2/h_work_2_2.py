# Task_2
# Написать функцию my_enumerate.
# Вход: list
# Выход: list из кортежей в каждом из которыйх два элемента - первый это индекс исходного списка,
# вторая элемент исходного списка с индексом.
# Встроенную функцию enumerate использовать нельзя, zip использовать можно, но необязательно.


# without ZIP

def my_enumerate_no_zip(some_list):
    tuple_list = [(i, (some_list[i])) for i in range(len(some_list))]
    return tuple_list


# with ZIP
def my_enumerate_with_zip(some_list):
    idx_list = [i for i in range(len(some_list))]
    tuple_list = [(idx, val) for idx, val in zip(idx_list, some_list)]
    return tuple_list


def main():
    source_list = list(range(2, 100 + 1))
    result_list_zip = my_enumerate_with_zip(source_list)
    result_list_no_zip = my_enumerate_no_zip(source_list)
    print(result_list_zip)
    print(result_list_no_zip)


main()