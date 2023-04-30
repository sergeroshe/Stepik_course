def find_all(source, symbol):

    symbol_idx_list = []
    start_idx = 0
    symbol_idx = source.find(symbol, start_idx)

    while symbol_idx != -1:  #remove break -1 in loop header
        symbol_idx_list.append(symbol_idx)
        start_idx = symbol_idx + 1
        symbol_idx = source.find(symbol, start_idx)

    return symbol_idx_list


def main():
    source_string = input()
    char = input()
    symbol_occur_list = find_all(source_string, char)
    print(symbol_occur_list)


main()



# def find_all(source, symbol):
#
#     symbol_idx_list = []
#     start_idx = 0
#     len_source = len(source)
#
#     while start_idx <= len_source - 1:
#         symbol_idx = source.find(symbol, start_idx)
#         if symbol_idx == -1:
#             break
#         else:
#             symbol_idx_list.append(symbol_idx)
#             start_idx = symbol_idx + 1
#
#     return symbol_idx_list