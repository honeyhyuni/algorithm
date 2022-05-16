# https://www.acmicpc.net/problem/18290
import sys

input = sys.stdin.readline
n, m, k = map(int, input().split())
arr = [list(map(int, input().split())) for i in range(n)]

# 2차원 배열의 크기 만큼(n*m) 인덱스를 담은 배열
lst = [[i, j] for i in range(n) for j in range(m)]
result = []
min_v = -sys.maxsize


def back(idx):
    global min_v
    if len(result) == k:
        temp = 0
        for i in range(k):
            x, y = result[i]
            temp += arr[x][y]
            for j in range(k):
                x2, y2 = result[j]
                if abs(x - x2) + abs(y - y2) == 1:  # 인접 불가능
                    return
        min_v = max(min_v, temp)
        return
    for i in range(idx, len(lst)):
        result.append(lst[i])
        back(i + 1)
        result.pop()
    return min_v


print(back(0))
