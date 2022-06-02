# https://www.acmicpc.net/problem/4195
import sys

sys.setrecursionlimit(10 ** 5)


def find_parent(var):
    if var != relation[var]:
        relation[var] = find_parent(relation[var])
    return relation[var]


def union(x, y):
    x_n = find_parent(x)
    y_n = find_parent(y)

    if x_n == y_n:
        return

    relation[y_n] = x_n
    visited[x_n] += visited[y_n]


input = sys.stdin.readline
T = int(input())
for t in range(T):
    N = int(input())
    relation = {}
    visited = {}
    for n in range(N):
        x, y = map(str, input().split())
        if x not in relation:
            relation[x] = x
            visited[x] = 1
        if y not in relation:
            relation[y] = y
            visited[y] = 1
        union(x, y)
        print(visited[find_parent(x)])
