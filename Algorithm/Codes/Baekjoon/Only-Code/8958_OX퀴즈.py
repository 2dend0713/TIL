import sys


T = int(sys.stdin.readline())

for _ in range(T):
    result = sys.stdin.readline()

    ans, acc = 0, 1
    for char in result:
        if char == "O":
            ans += acc
            acc += 1
        else:
            acc = 1

    print(ans)
