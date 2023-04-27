   # объявление функции
def merge(list1, list2):
    result_list = list1 + list2
    for i in range(len(result_list)):
        min_num = result_list[i]
        min_num_idx = i
        for j in range(i + 1, len(result_list)):
            if result_list[j] < min_num:
                min_num = result_list[j]
                min_num_idx = j
        result_list[i], result_list[min_num_idx] = result_list[min_num_idx], result_list[i]
    return result_list


def main():
   # считываем данные
    num_list_1 = [int(c) for c in input().split()]
    num_list_2 = [int(c) for c in input().split()]
    print(merge(num_list_1, num_list_2))


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