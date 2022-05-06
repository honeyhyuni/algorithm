# https://www.acmicpc.net/problem/9466
import sys

sys.setrecursionlimit(10 ** 5)
input = sys.stdin.readline


def dfs(idx):
    global result
    visited[idx] = True
    value = arr[idx]
    temp.append(idx)
    if visited[value]:
        if value in temp:
            result += temp[temp.index(value):]
        return
    else:
        dfs(value)


T = int(input())
for t in range(T):
    n = int(input())
    arr = [0] + list(map(int, input().split()))
    visited = [False] * (n + 1)
    result = []
    for i in range(1, n + 1):
        if not visited[i]:
            temp = []
            dfs(i)
    print(n - len(result))
