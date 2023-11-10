MATRIX_SIZE = 8
CHESS_KNIGHT_POSITION_MARK = 'N'
POSSIBLE_MOVE_MARK = '*'

matrix = []

position = 'b6'
# position = input()
knight_x = ord(position[0]) - 97
knight_y = MATRIX_SIZE - int(position[-1])

for i in range(MATRIX_SIZE):
    row = ''
    for j in range(MATRIX_SIZE):
        # if i == 2 and j == 1:
        if abs(knight_x - j) + abs(knight_y - i) == 0:
            row += 'K '
        elif (knight_y - i) * (knight_x - j) in [-2, 2]: #
            row += '* '
        else:
            row += '. '
    print(row.rstrip())

# for _ in range(MATRIX_SIZE):
#     matrix.append('. . . . . . . .'.split())
# move_1 = [knight_x + 2, knight_y + 1]
# move_2 = [knight_x + 2, knight_y - 1]
# move_3 = [knight_x - 2, knight_y + 1]
# move_4 = [knight_x - 2, knight_y - 1]
# move_5 = [knight_x + 1, knight_y + 2]
# move_6 = [knight_x + 1, knight_y - 2]
# move_7 = [knight_x - 2, knight_y + 1]
# move_8 = [knight_x - 2, knight_y - 1]


# matrix[knight_y][knight_x] = CHESS_KNIGHT_POSITION_MARK
#
# for row in matrix:
#     print(*row)
