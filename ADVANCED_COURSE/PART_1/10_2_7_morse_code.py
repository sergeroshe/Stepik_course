LETTERS = [c for c in 'ABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789']
MORSE = ['.-', '-...', '-.-.', '-..', '.',
         '..-.', '--.', '....', '..', '.---',
         '-.-', '.-..', '--', '-.', '---', '.--.',
         '--.-', '.-.', '...', '-', '..-', '...-',
         '.--', '-..-', '-.--', '--..', '-----',
         '.----', '..---', '...--', '....-', '.....',
         '-....', '--...', '---..', '----.']

MORSE_CODE_DICT = {LETTERS[i]: MORSE[i] for i in range(len(LETTERS))}

morse_code_dict_len = len(MORSE_CODE_DICT)

input_string = input().upper()
# input_string = 'Agent 007'.upper()

output_string = ''


for char in input_string:
    if char in MORSE_CODE_DICT:
        output_string += ' ' + MORSE_CODE_DICT[char]

print(output_string)

