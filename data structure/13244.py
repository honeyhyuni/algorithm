# https://www.acmicpc.net/problem/13244
import sys
input = sys.stdin.readline
T = int(input())


def find_parent(x):
    if x != parent[x]:
        parent[x] = find_parent(parent[x])
    return parent[x]


def union(a, b):
    a_n, b_n = find_parent(a), find_parent(b)
    if a_n != b_n:
        if a_n < b_n:
            parent[b_n] = a_n
        else:
            parent[a_n] = b_n
        return True
    else:
        return False


for t in range(T):
    n = int(input())
    m = int(input())
    parent = [i for i in range(n + 1)]
    bol = True
    for i in range(m):
        a, b = map(int, input().split())
        if not union(a, b):
            bol = False

    if not bol:
        print("graph")
    else:
        for i in range(1, n+1):
            if find_parent(parent[i]) != 1:
                print("graph")
                break
        else:
            print("tree")