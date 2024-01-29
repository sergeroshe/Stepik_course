
def get_mtrx_square_pow(mtrx_1, mtrx_2):
    result_matrix = []
    mtrx_1_rows = len(mtrx_1)
    mtrx_1_cols = len(mtrx_1[0])
    mtrx_2_cols = len(mtrx_2[0])

    for k in range(mtrx_1_rows):
        row = []
        for i in range(mtrx_2_cols):
            row_element = 0
            for j in range(mtrx_1_cols):
                row_element += mtrx_1[k][j] * mtrx_2[j][i]
            row.append(row_element)
        result_matrix.append(row)
    return result_matrix


def main():
    matrix_size = int(input())
    matrix = []
    for _ in range(matrix_size):
        row = [int(el) for el in input().split()]
        matrix.append(row)
    matrix_power = int(input())
    matrix_size = len(matrix)
    powered_matrix = matrix

    for _ in range(matrix_power - 1):
        powered_matrix = get_mtrx_square_pow(powered_matrix, matrix)

    for i in range(matrix_size):
        for j in range(matrix_size):
            print(str(powered_matrix[i][j]).ljust(3), end=' ')
        print()


main()


# matrix = [[1, 2, 1],
#           [3, 3, 3],
#           [1, 2, 1]]

# matrix = [[1, 2, 1],
#           [3, 3, 3],
#           [1, 2, 1]]

# matrix = [[1, 2, 3],
#           [4, 5, 6],
#           [7, 8, 9]]
