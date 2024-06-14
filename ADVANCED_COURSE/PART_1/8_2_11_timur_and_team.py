sea_visitors = int(input())
village_visitors = int(input())
mountains_visitors = int(input())
village_and_sea_visitors = int(input())
village_and_mountains_visitors = int(input())
nowhere_visitors = int(input())

only_sea_visitors = sea_visitors - village_and_sea_visitors
only_village_visitors = village_visitors - village_and_mountains_visitors - village_and_sea_visitors
only_mountains_visitors = mountains_visitors - village_and_mountains_visitors

total_people = only_sea_visitors + only_village_visitors + only_mountains_visitors\
               + village_and_mountains_visitors + village_and_sea_visitors + nowhere_visitors

print(total_people)