countries_info_amount = int(input())

countries_info_dict = {}
for _ in range(countries_info_amount):
    country, *cities = input().split()
    countries_info_dict[country] = cities

cities_amount = int(input())
cities_list = [input() for _ in range(cities_amount)]

countries_list = []

for city in cities_list:
    for country, cities in countries_info_dict.items():
        if city in cities:
            countries_list.append(country)
            break

print(*countries_list, sep='\n')

