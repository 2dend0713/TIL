def solution(N, number):
    nums = [[int(str(N) * cnt)] for cnt in range(1, 9)]

    for cnt in range(1, 8):
        for case in range(cnt):
            for num_first in nums[case]:
                for num_second in nums[cnt-case-1]:
                    nums[cnt].append(num_first + num_second)
                    nums[cnt].append(num_first - num_second)
                    nums[cnt].append(num_first * num_second)
                    if num_second:
                        nums[cnt].append(num_first / num_second)

    for idx, num_li in enumerate(nums):
        if number in set(num_li):
            return idx + 1
    else:
        return -1

print(solution(5, 12))
print(solution(2, 11))
