# https://www.acmicpc.net/problem/25602
import sys
input = sys.stdin.readline
n, k = map(int, input().split())
value = list(map(int, input().split()))
arr = [list(map(int, input().split())) for i in range(k * 2)]
visited = [False] * (k*2)
result = 0


def back(cnt, v):
    global result
    if cnt == k * 2:
        result = max(result, v)
        return
    for i in range(cnt, k*2):
        for j in range(n):
            if visited[i] or value[j] == 0:
                continue
            visited[i] = True
            value[j] -= 1
            back(cnt + 1, v + arr[i][j])
            visited[i] = False
            value[j] += 1


back(0, 0)
print(result)