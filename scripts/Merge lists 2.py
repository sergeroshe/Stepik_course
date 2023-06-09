def quick_merge(list_1, list_2):
    sort_result = []

    list_1_num_idx = 0  # указатель на первый элемент списка list1
    list_2_num_idx = 0  # указатель на первый элемент списка list2
    list_1_len = len(list_1)
    list_2_len = len(list_2)

    while list_1_num_idx < list_1_len and list_2_num_idx < list_2_len:  # пока не закончился хотя бы один список
        if list_1[list_1_num_idx] <= list_2[list_2_num_idx]:
            sort_result.append(list_1[list_1_num_idx])
            list_1_num_idx += 1
        else:
            sort_result.append(list_2[list_2_num_idx])
            list_2_num_idx += 1

    if list_1_num_idx < len(list_1):  # прицепление остатка
        sort_result += list_1[list_1_num_idx:]
    elif list_2_num_idx < len(list_2):
        sort_result += list_2[list_2_num_idx:]

    return sort_result


def main():
    result_list = []
    n = int(input())

    for _ in range(n):
        current_list = [int(num) for num in input().split()]
        result_list = quick_merge(result_list, current_list)

    print(*result_list)
# a b c d
# A c d
# B d


main()
# unsorted_list = ['10 20', '1 15', '5 17', '8 13 19']

# Merge lists 2
# На вход программе подается число
# �
# n, а затем
# �
# n строк, содержащих целые числа в порядке возрастания. Из данных строк формируются списки чисел. Напишите программу, которая объединяет указанные списки
# в один отсортированный список с помощью функции quick_merge(), а затем выводит его.
#
# Формат входных данных
# На вход программе подается натуральное число
# �
# n, а затем
# �
# n строк, содержащих целые числа в порядке возрастания, разделенные символом пробела.
#
# Формат выходных данных
# Программа должна вывести текст в соответствии с условием задачи.