import sys

chars = list(sys.stdin.readline().rstrip())

chars_cnt = [0] * 26
std_lower, std_upper = ord('a'), ord('A')
for char in chars:
    if 'a' <= char <= 'z':
        chars_cnt[ord(char) - std_lower] += 1
    elif 'A' <= char <= 'Z':
        chars_cnt[ord(char) - std_upper] += 1

max_cnt = max(chars_cnt)
flag, idx = 0, -1
for i, cnt in enumerate(chars_cnt):
    if cnt == max_cnt:
        flag, idx = flag + 1, i

if flag == 1:
    print(chr(idx+ std_upper))
else:
    print('?')
