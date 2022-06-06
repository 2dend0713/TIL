import sys


MELODY = list(map(int, sys.stdin.readline().split()))

first_sound = MELODY[0]
if first_sound == 1:
    result = 'ascending'
    for m in range(7):
        if MELODY[m] > MELODY[m+1]:
            result = 'mixed'
elif first_sound == 8:
    result = 'descending'
    for m in range(7):
        if MELODY[m] < MELODY[m+1]:
            result = 'mixed'
else:
    result = 'mixed'

print(result)
