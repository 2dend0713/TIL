import sys


def get_num(row, col):
    border = max(abs(row), abs(col))  # 해당 좌표가 속하는 테두리 파악
    dist_rt = abs(row+border) + abs(col-border)
    dist_lb = abs(row-border) + abs(col+border)

    # 우상단 꼭짓점과 더 까깝다면
    if dist_rt <= dist_lb:
        std = 4 * border ** 2 - 2 * border + 1
        # 두 꼭짓점과의 사이 거리가 같다면
        if dist_rt == dist_lb:
            return (2 * border + 1) ** 2 if border == row else std + dist_rt
        return std + dist_rt if border == abs(row) else std - dist_rt
    # 좌하단 꼭짓점과 더 가깝다면
    elif dist_rt > dist_lb:
        std = 4 * border ** 2 + 2 * border + 1
        return std + dist_lb if border == abs(row) else std - dist_lb


def add_spaces(num):
    global len_max_num
    return ' ' * (len_max_num - len(str(num))) + str(num)


R1, C1, R2, C2 = map(int, sys.stdin.readline().split())
offset = 0 - R1
paper = [[] for _ in range(R2 - R1 + 1)]

max_num = 0
for r in range(R1, R2+1):
    for c in range(C1, C2+1):
        num = get_num(r, c)  # 좌표에 해당하는 수 찾기
        max_num = max(max_num, num)  # 가장 큰 수 저장하기
        paper[r+offset].append(num)

len_max_num = len(str(max_num))
for row in paper:
    print(' '.join(map(add_spaces, row)))  # 오른쪽 정렬해서 출력하기
