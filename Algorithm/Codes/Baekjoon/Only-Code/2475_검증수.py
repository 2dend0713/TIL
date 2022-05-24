import sys


num = sum(map(lambda x: x ** 2, map(int, sys.stdin.readline().split(' ')))) % 10
print(num)
