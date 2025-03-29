text = 'footballcyberpunkextraterritorial' \
       'ityconversationalistblockophthal' \
       'moscopicinterdependencemamauserfff'

result = {}

for char in text:
    if char not in result:
        result[char] = text.count(char)

print(result)