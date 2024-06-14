b_1, b_2, b_3, b_1_or_b_2, b_2_or_b_3, b_1_or_b_3, all_books_read, total_people = [int(input()) for el in range(8)]
# b_1, b_2, b_3, b_1_or_b_2, b_2_or_b_3, b_1_or_b_3, all_books_read, total_people = [19, 18, 22, 32, 33, 35, 2, 50]

only_b_1_and_b_2 = b_2 + b_1 - b_1_or_b_2 - all_books_read
only_b_2_and_b_3 = b_2 + b_3 - b_2_or_b_3 - all_books_read
only_b_1_and_b_3 = b_1 + b_3 - b_1_or_b_3 - all_books_read

two_books_read = only_b_1_and_b_2 + only_b_2_and_b_3 + only_b_1_and_b_3

only_book_1_read = b_1 - only_b_1_and_b_2 - only_b_1_and_b_3 - all_books_read
only_book_2_read = b_2 - only_b_1_and_b_2 - only_b_2_and_b_3 - all_books_read
only_book_3_read = b_3 - only_b_1_and_b_3 - only_b_2_and_b_3 - all_books_read

one_book_read = only_book_1_read + only_book_2_read + only_book_3_read

none_books_read = total_people - one_book_read - two_books_read - all_books_read

print(two_books_read)
print(one_book_read)
print(none_books_read)
