## N으로 표현

<br>

#### 001. 첫 번째 풀이

> 개수를 늘려가면서 수를 만들어 가는 방식을 정리하면, 크게 1) 그냥 이어 붙이기, 2) 사칙연산으로 나눌 수 있다. 이때, 사칙연산의 경우, 앞서 만들어 놓은 수들을 활용한다는 점에 착안하여 각 연산 케이스를 4중 for문을 활용해서 구현하였다...

<br>

```python
def solution(N, number):
    nums = [set() for _ in range(8)]
    for idx, num_set in enumerate(nums):
        num_set.add(int(str(N) * (idx + 1)))

    for cnt in range(1, 8):
        for case in range(cnt):
            for num_first in nums[case]:
                for num_second in nums[cnt-case-1]:
                    nums[cnt].add(num_first + num_second)
                    nums[cnt].add(num_first - num_second)
                    nums[cnt].add(num_first * num_second)
                    if num_second:
                        nums[cnt].add(num_first / num_second)

    for idx, num_set in enumerate(nums):
        if number in num_set:
            return idx + 1
    else:
        return -1
```

