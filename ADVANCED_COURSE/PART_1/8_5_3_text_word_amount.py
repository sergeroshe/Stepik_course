text_string = input()

word_set = set()
for word in text_string.split():
# use lstrip() method
    for letter in word:
        if not letter.isalpha():
            word = word.replace(letter, '')
    word_set.add(word.lower())
string_word_amount = len(word_set)

print(string_word_amount)

# string = 'Snowflakes, snowflakes falling down.' \
#          ' Snowflakes, covering up the ground.' \
#          ' Making a blanket, soft and white.' \
#          ' Making a blanket in the night.'
