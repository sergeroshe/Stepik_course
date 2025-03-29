country_info_amount = int(input())
country_info_dict = {country: cities for _ in range(country_info_amount)
                     for country, *cities in [input().split()]}

city_amount = int(input())
city_list = [input() for _ in range(city_amount)]

countries_list = []

for city in city_list:
    for country, cities in country_info_dict.items():
        if city in cities:
            countries_list.append(country)
            break

print(*countries_list, sep='\n')
