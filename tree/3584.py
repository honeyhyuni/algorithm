# https://www.acmicpc.net/problem/3584 
# 가장 가까운 공통조상(LCA, lowest common ancestor) 이론 문제
import sys
input = sys.stdin.readline
sys.setrecursionlimit(10**5)
T = int(input())
for t in range(T):
    n = int(input())
    parent = [0] * (n+1)
    for i in range(n-1):
        x, y= map(int, input().split())
        parent[y] = x
    a, b = map(int, input().split())
    a_list, b_list = [0, a], [0, b]
    while parent[a]:
        a_list.append(parent[a])
        a = parent[a]

    while parent[b]:
        b_list.append(parent[b])
        b = parent[b]

    idx = 1
    while a_list[-idx] == b_list[-idx]:
        idx += 1

    print(a_list[-idx+1])