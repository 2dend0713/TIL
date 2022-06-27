## 🔥 11559 Puyo Puyo

> source: BOJ
>
> level: Gold 4
>
> link: https://www.acmicpc.net/problem/11559

<br />

<br />

### 001. 흐름

<br />

1. 입력값 순회

   1. 빈 공간

   1. 뿌요

      1. **인접한(상하좌우) 동일색의 뿌요 탐색 by BFS**

         1. 탐색한 뿌요 개수 ≥ 4
            1. 터뜨리기
         1. 탐색한 뿌요 개수 < 4

         <br />

1. `1`에 대한 상황 판단

   1. 터뜨린 뿌요가 존재하지 않음
      1. 결과값 반환
   1. 터뜨린 뿌요가 존재함
      1. **중력 적용하기 using deque**
      1. `1` 반복

<br />

<br />

### 002. 코드

<br />

```python
import sys
from collections import deque

def search(row, col, color):
    global exploded
    candidates = [(row, col)]
    q = deque([(row, col)])

    while q:
        r, c = q.popleft()
        for d in range(4):
            nr, nc = r + dy[d], c + dx[d]
            if not (0 <= nr < 12 and 0 <= nc < 6) or visited[nr][nc]:
                continue
            if FIELD[nr][nc] == color:
                visited[nr][nc] = 1
                candidates.append((nr, nc))
                q.append((nr, nc))

    if len(candidates) >= 4:  # 4개 이상의 동일 색깔 뿌요가 모여 있다면
        for r, c in candidates:
            FIELD[r][c] = '.'
            exploded = 1

def move_down():
    for c in range(6):
        left = deque()  # 임시적으로 넣었다 빼기
        for r in range(11, -1, -1):
            if FIELD[r][c] != '.':
                left.append(FIELD[r][c])

        for r in range(11, -1, -1):
            if left:
                FIELD[r][c] = left.popleft()
            else:
                FIELD[r][c] = '.'

# input
FIELD = [list(sys.stdin.readline().rstrip()) for _ in range(12)]

# init
dy = [-1, 0, 1, 0]
dx = [0, 1, 0, -1]
result = 0

while True:
    exploded = False
    visited = [[0] * 6 for _ in range(12)]
    for r in range(12):
        for c in range(6):
            if FIELD[r][c] != '.' and not visited[r][c]:
                visited[r][c] = 1
                search(r, c, FIELD[r][c])  # BFS -> 터지는 뿌요 찾기

    if exploded:
        move_down()  # deque -> 중력 적용하기
        result += 1
    else:
        break

# output
print(result)
```

<br />

<br />

*End*

