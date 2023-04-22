   # объявление функции
def merge(list1, list2):
    common_list = list1 + list2
    for i in range(len(common_list)):
        min_num = common_list[i]
        min_num_idx = i
        for j in range(i + 1, len(common_list)):
            if common_list[j] < min_num:
                min_num = common_list[j]
                min_num_idx = j
        common_list[i], common_list[min_num_idx] = common_list[min_num_idx], common_list[i]
    return common_list


def main():
   # считываем данные
    numbers1 = [int(c) for c in input().split()]
    numbers2 = [int(c) for c in input().split()]
    print(merge(numbers1, numbers2))


main()

# Merge lists 1
# Напишите функцию merge(list1, list2), которая принимает в качестве аргументов два отсортированных по возрастанию списка, состоящих из целых чисел, и объединяет их в один отсортированный список.
#
# Примечание 1. Списки list1 и list2 могут иметь разную длину.
#
# Примечание 2. Можно использовать списочный метод sort(), а можно обойтись и без него 😎.
#
# Примечание 3. Следующий программный код:
#
# print(merge([1, 2, 3], [5, 6, 7, 8]))
# print(merge([1, 7, 10, 16], [5, 6, 13, 20]))
# должен выводить:

# [1, 2, 3, 5, 6, 7, 8]
# [1, 5, 6, 7, 10, 13, 16, 20]