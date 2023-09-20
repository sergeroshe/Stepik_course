source_string_list = input().split()
chunk_size = int(input())
# source_string_list = 'a b c d e f r g b'.split()
# chunk_size = 4

total_list = [source_string_list[i: i + chunk_size] for i in range(0, len(source_string_list), chunk_size)]

print(total_list)
