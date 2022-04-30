# https://www.acmicpc.net/status?user_id=tjfkqwkd001&problem_id=2661&from_mine=1
n = int(input())

result = []
arr = [1, 2, 3]


def back(cnt):
    for i in range(1, (cnt // 2) + 1):
        if result[-i:] == result[-2 * i:-i]:
            return 1
    if cnt == n:
        print("".join(map(str, result)))
        return 0
    for i in arr:
        result.append(i)
        if back(cnt + 1) == 0:
            return 0
        result.pop()


back(0)
