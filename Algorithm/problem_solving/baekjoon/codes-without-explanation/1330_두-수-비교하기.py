import sys


def compare(num1, num2):
    if num1 > num2:
        return '>'
    elif num1 < num2:
        return '<'
    elif num1 == num2:
        return '=='


a, b = map(int, sys.stdin.readline().split())
print(compare(a, b))
