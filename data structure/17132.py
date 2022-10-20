# https://www.acmicpc.net/problem/17132
import sys
input = sys.stdin.readline


def parent_find(v):
    if v != parent[v]:
        parent[v] = parent_find(parent[v])
    return parent[v]


def union(a, b, c):
    global result
    a_n = parent_find(a)
    b_n = parent_find(b)
    if a_n != b_n:
        parent[b_n] = a_n
        result += cnt[a_n] * cnt[b_n] * c
        cnt[a_n] += cnt[b_n]


n = int(input())
arr = []
parent = [i for i in range(n + 1)]
cnt = [1] * (n + 1)
for i in range(n - 1):
    a, b, c = map(int, input().split())
    arr.append((c, a, b))

arr.sort(key=lambda x: (-x[0], x[1], x[2]))
result = 0
for c, a, b in arr:
    union(a, b, c)

print(result)