import sys


def check_year(year):
    if (year % 4 == 0 and year % 100 != 0) or year % 400 == 0:
        return 1
    else:
        return 0


YEAR = int(sys.stdin.readline())

print(check_year(YEAR))
