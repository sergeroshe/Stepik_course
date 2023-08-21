SIGNATURE = 'anton'

fridge_number = int(input())

infected_fridge_list = []
fridge_string_list = []

[fridge_string_list.append(input()) for i in range(fridge_number)]

for i in range(len(fridge_string_list)):
    fridge_string = fridge_string_list[i]
    letters_found_list = []
    found_letter_idx = 0
    j = 0
    search_on = True
    while search_on:
        letter = SIGNATURE[j]
        found_letter_idx = fridge_string.find(letter, found_letter_idx)
        if found_letter_idx == -1:
            search_on = False
        elif j + 1 == len(SIGNATURE):
            infected_fridge_list.append(i + 1)
            search_on = False
        j += 1

print(*infected_fridge_list, sep=' ')
