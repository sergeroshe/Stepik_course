def find_all(source, symbol):

    symbol_idx_list = []
    count = 0

    while source.find(symbol) != -1:
        symbol_idx = source.find(symbol)
        symbol_idx_list.append(symbol_idx + count)
        source = source.replace(symbol, '', 1)
        count += 1

    return symbol_idx_list


def main():
    source_string = input()    # maybe source-string?
    char = input()
    symbol_occur_list = find_all(source_string, char)   # 'a'
    print(symbol_occur_list)


main()
