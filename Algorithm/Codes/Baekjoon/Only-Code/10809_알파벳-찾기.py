import sys


word = sys.stdin.readline().rstrip()

for order in range(97, 123):
    print(word.find(chr(order)), end=' ')
