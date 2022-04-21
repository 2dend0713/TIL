import sys
from collections import deque


def make_emoticons():
    time[1][0] = 0
    q = deque([(1, 0)])

    while q:
        m, c = q.popleft()

        if m + c <= s and time[m+c][c] == -1:
            time[m+c][c] = time[m][c] + 1
            q.append((m+c, c))
        if time[m][m] == -1:
            time[m][m] = time[m][c] + 1
            q.append((m, m))
        if m >= 1 and time[m-1][c] == -1:
            time[m-1][c] = time[m][c] + 1
            q.append((m-1, c))


s = int(sys.stdin.readline().rstrip())
time = [[-1] * (s + 1) for _ in range(s+1)]

make_emoticons()
seconds = []
for second in time[s]:
    if second != -1:
        seconds.append(second)
print(min(seconds))
