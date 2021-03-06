## π₯ 11559 Puyo Puyo

> source: BOJ
>
> level: Gold 4
>
> link: https://www.acmicpc.net/problem/11559

<br />

<br />

### 001. νλ¦

<br />

1. μλ ₯κ° μν

   1. λΉ κ³΅κ°

   1. λΏμ

      1. **μΈμ ν(μνμ’μ°) λμΌμμ λΏμ νμ by BFS**

         1. νμν λΏμ κ°μ β₯ 4
            1. ν°λ¨λ¦¬κΈ°
         1. νμν λΏμ κ°μ < 4

         <br />

1. `1`μ λν μν© νλ¨

   1. ν°λ¨λ¦° λΏμκ° μ‘΄μ¬νμ§ μμ
      1. κ²°κ³Όκ° λ°ν
   1. ν°λ¨λ¦° λΏμκ° μ‘΄μ¬ν¨
      1. **μ€λ ₯ μ μ©νκΈ° using deque**
      1. `1` λ°λ³΅

<br />

<br />

### 002. μ½λ

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

    if len(candidates) >= 4:  # 4κ° μ΄μμ λμΌ μκΉ λΏμκ° λͺ¨μ¬ μλ€λ©΄
        for r, c in candidates:
            FIELD[r][c] = '.'
            exploded = 1

def move_down():
    for c in range(6):
        left = deque()  # μμμ μΌλ‘ λ£μλ€ λΉΌκΈ°
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
                search(r, c, FIELD[r][c])  # BFS -> ν°μ§λ λΏμ μ°ΎκΈ°

    if exploded:
        move_down()  # deque -> μ€λ ₯ μ μ©νκΈ°
        result += 1
    else:
        break

# output
print(result)
```

<br />

<br />

*End*

