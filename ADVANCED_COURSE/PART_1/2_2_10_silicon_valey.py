SIGNATURE = 'anton'
fridge_number = int(input())
# fridge_number = 2
# fridge_string_list = ['gftcfajkunytftttit7yjoogo87tfo898ynoctu', 'n8yt68r5dyotnakvbug6o86']
infected_fridge_list = []
fridge_string_list = []

[fridge_string_list.append(input()) for i in range(fridge_number)]

for i in range(len(fridge_string_list)):
    fridge_string = fridge_string_list[i]
    letters_found_list = []
    found_letter_idx = 0
    if fridge_string.find(SIGNATURE[0]) != -1 and fridge_string.rfind(SIGNATURE[-1]) != -1:
        for j in range(len(SIGNATURE)):
            letter = SIGNATURE[j]
            found_letter_idx = fridge_string.find(letter, found_letter_idx)
            if found_letter_idx == -1 and j != len(fridge_string):
                break
            else:
                if j + 1 == len(SIGNATURE):
                    infected_fridge_list.append(i + 1)

print(*infected_fridge_list, sep=' ')
