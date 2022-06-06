import sys


def calculate(operators, n):
    queue = []
    nums = list(range(1, n+1))

    for idx in range(n-1):
        if operators[idx] == ' ':
            nums[idx+1] = int(str(nums[idx]) + str(nums[idx+1]))
        else:
            queue += [nums[idx], operators[idx]]
    queue.append(nums[idx+1])

    result, expr = queue[0], ' '.join(str(queue[0]))
    for idx in range((len(queue)-1)//2):
        if queue[2*idx+1] == '+':
            result += queue[2*idx+2]
            expr += '+' + ' '.join(str(queue[2*idx+2]))
        else:
            result -= queue[2*idx+2]
            expr += '-' + ' '.join(str(queue[2*idx+2]))

    if result == 0:
        cases.append(expr)


def find_cases(n, step=0, operators=[]):
    if step == n-1:
        calculate(operators, n)
        return

    for operator in [' ', '+', '-']:
        find_cases(n, step+1, operators+[operator])


T = int(sys.stdin.readline().rstrip())
for _ in range(T):
    N = int(sys.stdin.readline().rstrip())

    cases = []
    find_cases(N)
    cases.sort()

    for case in cases:
        print(case)
    print()
