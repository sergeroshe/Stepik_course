from decimal import Decimal

num = Decimal(input())

min_dig = 0
max_dig = max(num.as_tuple()[1])

if int(num):
    min_dig = min(num.as_tuple()[1])

max_min_number_dig_sum = sum([min_dig, max_dig])

print(max_min_number_dig_sum)

num = Decimal('0.1244354689')
