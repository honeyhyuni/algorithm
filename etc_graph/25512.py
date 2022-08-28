# https://www.acmicpc.net/problem/25512
import sys
sys.setrecursionlimit(10**5)
input = sys.stdin.readline


def dfs(v, w_b):
    global temp
    temp += v_[v][w_b]
    for i in arr[v]:
        dfs(i, 1 - w_b)


n = int(input())
arr = [[] for i in range(n)]
for i in range(n - 1):
    a, b = map(int, input().split())
    arr[a].append(b)

v_ = [list(map(int, input().split())) for i in range(n)]

result = sys.maxsize
temp = 0
dfs(0, 0)
result = min(result, temp)
temp = 0
dfs(0, 1)
print(min(result, temp))
