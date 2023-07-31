num = int(input())
num_string = str(num)
reversed_num_part_string = num_string[-5:][::-1]
unchangeable_num_part = num_string[:-5]
result_num_string = unchangeable_num_part + reversed_num_part_string
result_num = int(result_num_string)

print(result_num)
