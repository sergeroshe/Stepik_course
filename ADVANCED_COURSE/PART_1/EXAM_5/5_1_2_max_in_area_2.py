
def mtrx_fill(rows):
    mtrx = []
    for _ in range(rows):
        row = [int(el) for el in input().split()]
        mtrx.append(row)
    return mtrx


def mtrx_right_lower_corner(mtrx):
    max_num = mtrx[0][-1]
    rows = len(mtrx)
    cols = len(mtrx[0])
    for i in range(rows):
        shift = i + cols if rows - i >= cols else rows
        for j in range(i, shift):
            num = mtrx[j][-1 - (j - i)]
            if num > max_num:
                max_num = num

    return max_num


def main():
    mtrx_size = int(input())
    mtrx = mtrx_fill(mtrx_size)

    max_num = mtrx_right_lower_corner(mtrx)

    print(max_num)

main()