import sys


def check_valid(num, row, col):
    for idx in range(9):
        if BOARD[row][idx] == num:
            return False
        if BOARD[idx][col] == num:
            return False

    sect_row, sect_col = row // 3, col // 3
    for r in range(sect_row*3, (sect_row+1)*3):
        for c in range(sect_col*3, (sect_col+1)*3):
            if BOARD[r][c] == num:
                return False

    return True


def set_num(zeros_cnt, step=0):
    global flag

    if step == zeros_cnt:
        for row in BOARD:
            print(''.join(map(str, row)))
        flag = True
        return

    row, col = zeros[step]
    for num in range(1, 10):
        if check_valid(num, row, col):
            BOARD[row][col] = num
            set_num(zeros_cnt, step+1)
        if flag:
            return
    BOARD[row][col] = 0


BOARD = [list(map(int, list(sys.stdin.readline().rstrip()))) for _ in range(9)]
zeros = [(r, c) for r in range(9) for c in range(9) if BOARD[r][c] == 0]
zeros_cnt = len(zeros)
flag = False

set_num(zeros_cnt)
