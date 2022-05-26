import sys
from collections import deque


def perform(orders, target):
    r_cnt = 0

    for order in orders:
        # "뒤집기" 연산 횟수 집계
        if order == 'R':
            r_cnt += 1
        elif order == 'D':
            if len(target) == 0:
                return 'error'

            # 뒤집어져 있다면 맨 뒤의 원소 제거, 그렇지 않다면 맨 앞의 원소 제거
            if r_cnt % 2:
                target.pop()
            else:
                target.popleft()

    # 출력 형식 정확하게 맞추기
    return "[" + ",".join(reversed(target)) + "]" if r_cnt % 2 else "[" + ",".join(target) + "]"


T = int(sys.stdin.readline().rstrip())
for _ in range(T):
    P = list(sys.stdin.readline().rstrip())
    N = int(sys.stdin.readline().rstrip())
    ARR = sys.stdin.readline().rstrip()[1:-1].split(',')
    if N == 0:
        ARR = []

    print(perform(P, deque(ARR)))
