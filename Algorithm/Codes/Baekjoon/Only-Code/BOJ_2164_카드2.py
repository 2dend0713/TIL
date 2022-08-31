import sys
from collections import deque

nums = deque(num for num in range(1, int(sys.stdin.readline())+1))

while len(nums) != 1:
    nums.popleft()
    card_top = nums.popleft()
    nums.append(card_top)

print(nums[0])
