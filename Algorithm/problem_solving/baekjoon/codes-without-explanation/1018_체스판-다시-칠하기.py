import sys


def get_opposite(color):
    if color == 'W':
        return 'B'
    elif color == 'B':
        return 'W'


def count(line, color, other_color):
    cnt = 0
    for idx, cell in enumerate(line):
        if idx % 2 == 0 and not cell == color:
            cnt += 1
        elif idx % 2 == 1 and not cell == other_color:
            cnt += 1
    return cnt


def check_board(board, color, other_color):
    sum = 0
    for idx in range(0, 8):
        if idx % 2 == 0:
            sum += count(board[idx], color, other_color)
        elif idx % 2 == 1:
            sum += count(board[idx], other_color, color)
    return sum


n, m = map(int, sys.stdin.readline().split())
board = [list(sys.stdin.readline().rstrip()) for _ in range(n)]

ans = 8 * 8
for row in range(0, n-7):
    for col in range(0, m-7):
        new_board = [line[col:col+8] for line in board[row:row+8]]
        ans = min(check_board(new_board, new_board[0][0], get_opposite(new_board[0][0])), ans)
        ans = min(check_board(new_board, get_opposite(new_board[0][0]), new_board[0][0]), ans)

print(ans)
