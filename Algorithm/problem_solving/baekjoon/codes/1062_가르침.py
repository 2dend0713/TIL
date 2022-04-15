import sys


def pick_chars(idx=0, step=0):
    global ans

    if step == k - 5:
        cnt = 0
        for word in words:
            flag = 1
            for char in word:
                if not chars[ord(char)-97]:
                    flag = 0
            if flag:
                cnt += 1
        ans = max(ans, cnt)
        return

    for c in range(idx, 26):
        if not chars[c]:
            chars[c] = 1
            pick_chars(c, step+1)
            chars[c] = 0


n, k = map(int, sys.stdin.readline().split())
words = []
for _ in range(n):
    words.append(set(sys.stdin.readline().rstrip()))

default_chars = ['a', 'c', 'i', 'n', 't']
chars = [0] * 26
for char in default_chars:
    chars[ord(char)-97] = 1

ans = 0
if k < 5:
    print(0)
elif k == 26:
    print(n)
else:
    pick_chars()
    print(ans)
