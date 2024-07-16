INFO_DICT = [{'CS101': '3004, Хайнс 8:00'},
             {'CM241': '1411, Ли, 13:00'},
             {'CS102': '4501, Альварадо, 9:00'},
             {'NT110': '1244, Берк, 11:00'},
             {'CS103': '6755, Рич, 10:00'}
             ]
info_dict_len = len(INFO_DICT)

input_string = input()

selected_dict = {}
output_string = ''

string_not_found = True

i = 0
while string_not_found and i < info_dict_len:
    if input_string in INFO_DICT[i]:
        selected_dict = INFO_DICT[i]
        output_string = f'{input_string}: {selected_dict[input_string]}'
        string_not_found = False
    i += 1

print(output_string)