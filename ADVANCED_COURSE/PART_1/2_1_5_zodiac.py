ZODIAC_YEARS_LIST = ['Дракон', 'Змея', 'Лошадь', 'Овца', 'Обезьяна', 'Петух',
                     'Собака', 'Свинья', 'Крыса', 'Бык', 'Тигр', 'Заяц']
FIRST_ZODIAC_YEAR = 8
YEAR_CYCLE = 12

year = int(input())
zodiac_year_idx = ((year - FIRST_ZODIAC_YEAR) % YEAR_CYCLE)
zodiac_year = ZODIAC_YEARS_LIST[zodiac_year_idx]
print(zodiac_year)
