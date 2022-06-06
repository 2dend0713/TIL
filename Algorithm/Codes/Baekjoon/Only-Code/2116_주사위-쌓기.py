import sys


def get_dice_values(val, dice):
    idx = -1
    for s in range(6):
        if dice[s] == val:
            idx = s

    if idx == 0 or idx == 5:
        return max(dice[1], dice[2], dice[3], dice[4]), dice[(idx+5)%10]
    elif idx == 1 or idx == 3:
        return max(dice[0], dice[2], dice[4], dice[5]), dice[(idx+2)%4]
    elif idx == 2:
        return max(dice[0], dice[1], dice[3], dice[5]), dice[4]
    elif idx == 4:
        return max(dice[0], dice[1], dice[3], dice[5]), dice[2]


N = int(sys.stdin.readline().rstrip())
DICES = [list(map(int, sys.stdin.readline().split())) for _ in range(N)]

result = 0
for init in range(1, 7):
    sum, val, rep = 0, init, 0
    while rep < N:
        max_side_val, top_val = get_dice_values(val, DICES[rep])
        sum, val, rep = sum + max_side_val, top_val, rep + 1
    result = max(result, sum)

print(result)
