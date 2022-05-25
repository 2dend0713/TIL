import sys


nums = [int(sys.stdin.readline().rstrip()) for _ in range(9)]
max_num = max(nums)

print(max_num)
print(nums.index(max_num) + 1)
