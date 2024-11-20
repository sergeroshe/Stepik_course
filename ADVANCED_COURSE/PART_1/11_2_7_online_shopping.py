string_amount = int(input())
sale_string_list = [input() for _ in range(string_amount)]

sale_string_dict = {}
for sale_string in sale_string_list:
    name, item, amount = sale_string.split()
    sale_string_dict.setdefault(name, {})
    sale_string_dict[name][item] = sale_string_dict[name].get(item, 0) + int(amount)

result_sale_list = []
for name, items in sorted(sale_string_dict.items()):
    result_sale_list.append(f'{name}:')
    for item, amount in sorted(items.items()):
        result_sale_list.append(f'{item} {amount}')

print(*result_sale_list, sep='\n')

# sale_string_list = ['Руслан Пирог 1',
#                     'Тимур Карандаш 5',
#                     'Руслан Линейка 2',
#                     'Тимур Тетрадь 12',
#                     'Руслан Хлеб 3']