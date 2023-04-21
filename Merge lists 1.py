   # объявление функции
def merge(list1, list2):
    final_list = list1 + list2
    for i in range(len(final_list)):
        min_num = final_list[i]
        min_num_idx = i
        for j in range(i + 1, len(final_list)):
            if final_list[j] < min_num:
                min_num = final_list[j]
                min_num_idx = j
        final_list[i], final_list[min_num_idx] = final_list[min_num_idx], final_list[i]
    return final_list


def main():
   # считываем данные
    numbers1 = [int(c) for c in input().split()]
    numbers2 = [int(c) for c in input().split()]
    print(merge(numbers1, numbers2))


main()
