# https://www.acmicpc.net/problem/25515
import sys
sys.setrecursionlimit(10**5)
input = sys.stdin.readline


def dfs(node):
    for i in arr[node]:
        dfs(i)
        if v_[node] < v_[node] + v_[i]:
            v_[node] += v_[i]


n = int(input())
arr = [[] for i in range(n)]
for i in range(n - 1):
    a, b = map(int, input().split())
    arr[a].append(b)
v_ = list(map(int, input().split()))

dfs(0)
print(v_[0])
