# https://www.acmicpc.net/problem/25428
import sys

input = sys.stdin.readline


def parent_find(v):
    if v != parent[v]:
        parent[v] = parent_find(parent[v])
    return parent[v]


def union(a, b):
    global cnt
    a_n = parent_find(a)
    b_n = parent_find(b)
    if a_n != b_n:
        parent[a_n] = b_n
        cnt[b_n] += cnt[a_n]


n = int(input())
value = list(map(int, input().split()))
arr = [[] for i in range(n)]
parent = [i for i in range(n)]
for i in range(n - 1):
    a, b = map(int, input().split())
    arr[a - 1].append(b - 1)
    arr[b - 1].append(a - 1)
temp = []
for i, j in enumerate(value):
    temp.append((j, i))
temp.sort(key=lambda x: -x[0])

ans, cnt = 0, [1] * n

for i in range(n):
    now = temp[i][1]
    for next in arr[now]:
        if value[next] < value[now]:
            continue
        union(now, next)
    ans = max(ans, value[now] * cnt[parent_find(now)])
print(ans)
