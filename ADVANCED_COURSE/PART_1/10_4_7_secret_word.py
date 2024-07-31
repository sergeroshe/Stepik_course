encrypted_word_list = list(input())

char_freq_dict = {}
for i in range(len(encrypted_word_list)):
    char_freq_dict[encrypted_word_list[i]] = char_freq_dict.get(encrypted_word_list[i], 0) + 1

dict_letter_frequency = int(input())

letter_frequency_dict = {letter[0]: int(number) for _ in range(dict_letter_frequency)
                         for letter, number in [input().split()]}

decrypted_word_dict = {}
for char, char_freq in char_freq_dict.items():
    for letter, letter_freq in letter_frequency_dict.items():
        if char_freq == letter_freq:
            decrypted_word_dict[char] = letter

for i in range(len(encrypted_word_list)):
    for key, value in decrypted_word_dict.items():
        if encrypted_word_list[i] == key:
            encrypted_word_list[i] = value

print(*encrypted_word_list, sep='')


# dict_letter_frequency = 3
# letter_frequency_dict = {'а': 3, 'н': 2, 'с': 1}
# char_freq_dict = {'*': 3, '!': 2, '?': 1}
# encrypted_word_list = ['*', '!', '*', '!', '*', '?']
# encrypted_word = '*!*!*?'

# encrypted_word_list = list(encrypted_word)