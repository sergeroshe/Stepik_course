def find_all(source, symbol):

    symbol_idx_list = []
    count = 0
    len_source = len(source)

    while count < len_source:
        symbol_idx = source.find(symbol, count)
        if symbol_idx == -1:
            break
        else:
            symbol_idx_list.append(symbol_idx)
            count = symbol_idx + 1

    return symbol_idx_list


def main():
    source_string = input()
    char = input()
    symbol_occur_list = find_all(source_string, char)
    print(symbol_occur_list)


main()
