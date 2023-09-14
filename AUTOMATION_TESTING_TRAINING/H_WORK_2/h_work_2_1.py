# Task_1
# Напишите пожалуйста код для получения кортежа всех четных чисел от 2 до 100
# с использованием filter и lambda и второй вариант без использования filter и lambda.

# var_1: with filter, lambda

def get_odd_num_tuple_with_lambda(some_list):
    num_list = list(range(2, 100 + 1))
    odd_num_tuple = tuple(filter(lambda x: not x % 2, num_list))
    print(odd_num_tuple)


# var_2: without lambda, filter

def get_odd_num_tuple_no_lambda(some_list):
    return tuple(num for num in some_list if not num % 2)


def main():
    sample_list = list(range(2, 100 + 1))
    odd_num_tuple = tuple(filter(lambda x: not x % 2, sample_list))
    print(odd_num_tuple)
    odd_nums_in_tuple = get_odd_num_tuple_no_lambda(sample_list)
    print(odd_nums_in_tuple)


main()
