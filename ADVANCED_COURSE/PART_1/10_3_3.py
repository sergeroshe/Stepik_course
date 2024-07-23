text = 'footballcyberpunkextraterritorial' \
       'ityconversationalistblockophthal' \
       'moscopicinterdependencemamauserfff'

result = {}

for letter in text:
    if letter not in result:
        result[letter] = result.get(letter, 0) + text.count(letter)

print(result)