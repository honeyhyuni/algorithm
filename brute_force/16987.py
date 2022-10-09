# https://www.acmicpc.net/problem/16987
import sys
input = sys.stdin.readline
n = int(input())
arr = [list(map(int, input().split())) for i in range(n)]
result = 0


def back(c, idx):
    global result
    result = max(result, c)
    if idx == n:
        return
    for i in range(idx, n):
        if arr[i][0] <= 0:
            continue
        for j in range(n):
            if i == j or arr[j][0] <= 0:
                continue
            arr[i][0] -= arr[j][1]
            arr[j][0] -= arr[i][1]
            if arr[i][0] <= 0 and arr[j][0] <= 0:
                back(c + 2, i + 1)
            elif arr[i][0] <= 0 or arr[j][0] <= 0:
                back(c + 1, i + 1)
            else:
                back(c, i + 1)
            arr[i][0] += arr[j][1]
            arr[j][0] += arr[i][1]
        return


back(0, 0)
print(result)