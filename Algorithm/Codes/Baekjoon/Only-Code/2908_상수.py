import sys


A, B = sys.stdin.readline().split()
# print(f'A: {A}, B: {B}')

if A[::-1] >= B[::-1]:
    print(A[::-1])
else:
    print(B[::-1])
