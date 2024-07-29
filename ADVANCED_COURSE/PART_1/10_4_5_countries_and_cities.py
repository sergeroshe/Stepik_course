countries_info_amount = int(input())
countries_info_list = [input().split() for _ in range(countries_info_amount)]
cities_amount = int(input())
cities_list = [input() for _ in range(cities_amount)]

countries_info_dict = {}


for country, *cities in countries_info_list:
    countries_info_dict[country] = cities

countries_list = []


for city in cities_list:
    for country, cities in countries_info_dict.items():
        if city in cities:
            countries_list.append(country)
            break

print(*countries_list, sep='\n')
print(countries_info_dict)

# countries_info_amount = 2
# countries_info_list = ['Германия Берлин Мюнхен Гамбург Дортмунд',
#                        'Нидерланды Амстердам Гаага Роттердам Алкмар'
#                        ]
# cities_amount = 4
# cities_list = ['Амстердам', 'Алкмар', 'Гамбург', 'Гаага']
