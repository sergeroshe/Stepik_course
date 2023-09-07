input_string = input().split(' ')

sub_list = []
res_list = [[input_string[0]]]

for i in range(1, len(input_string)):
    if input_string[i] == input_string[i - 1]:
        res_list[-1].append(input_string[i])
    else:
        res_list.append([input_string[i]])

print(res_list)