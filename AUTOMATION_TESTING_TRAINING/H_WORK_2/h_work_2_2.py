# Task_2
# without ZIP

my_list = list(range(2, 100 + 1))
tuple_list = [(i, (my_list[i])) for i in range(len(my_list))]
print(tuple_list)
# with ZIP

my_list = list(range(2, 100 + 1))
idx_list = [i for i in range(len(my_list))]

tuple_list = [(idx, val) for idx, val in zip(idx_list, my_list)]
print(tuple_list)