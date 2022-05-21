# https://www.acmicpc.net/problem/1717
# union-find
import sys
sys.setrecursionlimit(10**5)
input = sys.stdin.readline

n, m = map(int, input().split())
arr = [i for i in range(n + 1)]


def find_parent(var):
    if var != arr[var]:
        arr[var] = find_parent(arr[var])
    return arr[var]


for i in range(m):
    check, a, b = map(int, input().split())
    a_n = find_parent(a)
    b_n = find_parent(b)
    if check == 0:
        if a_n != b_n:
            if a_n < b_n:
                arr[b_n] = a_n
            else:
                arr[a_n] = b_n
    else:
        if a_n != b_n:
            print("NO")
        else:
            print("YES")