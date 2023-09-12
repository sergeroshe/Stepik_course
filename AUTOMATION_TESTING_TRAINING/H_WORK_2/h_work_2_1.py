# Task_1
# var_1: with filter, lambda

num_list = list(range(2, 100 + 1))
odd_num_tuple = tuple(filter(lambda x: not x % 2, num_list))
print(odd_num_tuple)


# var_2: without lambda, filter

def get_odd_num_tuple(some_list):
    return tuple(num for num in some_list if not num % 2)


odd_nums_in_tuple = get_odd_num_tuple(num_list)
print(odd_nums_in_tuple)