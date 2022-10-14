# https://www.acmicpc.net/problem/17471
import sys
from itertools import combinations
from collections import deque


def bfs(nodes):
    q = deque()
    visited = [False for _ in range(n + 1)]
    visited[nodes[0]] = True
    q.append(nodes[0])
    while q:
        x = q.popleft()
        for i in range(1, len(arr[x])):
            if arr[x][i] == 0:
                continue
            if i not in nodes:
                continue
            if not visited[i]:
                visited[i] = True
                q.append(i)
    return visited.count(True) == len(nodes)


def plus_v(nodes):
    sum_v = 0
    for i in nodes:
        sum_v += people[i]
    return sum_v


n = int(input())
people = [0] + list(map(int, input().split()))
arr = [[0] * (n + 1) for i in range(n + 1)]
for i in range(1, n + 1):
    lst = list(map(int, input().split()))
    for l in range(lst[0]):
        arr[i][lst[l + 1]] = 1

min_v = sys.maxsize

su = {i for i in range(1, n + 1)}
for i in range(1, n // 2+1):
    A = list(set(combinations(su, i)))
    for a in A:
        B = list(set(su.difference(a)))
        if bfs(a) and bfs(B):
            sumA = plus_v(a)
            sumB = plus_v(B)
            min_v = min(min_v, abs(sumA - sumB))

if min_v >= sys.maxsize:
    print(-1)
else:
    print(min_v)
