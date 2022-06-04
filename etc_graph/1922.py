# https://www.acmicpc.net/problem/1922
import sys

input = sys.stdin.readline
n = int(input())
m = int(input())
arr = [i for i in range(n + 1)]
node = []
for i in range(m):
    x, y, z = map(int, input().split())
    node.append([x, y, z])
    node.append([y, x, z])


def find_parent(var):
    if var != arr[var]:
        arr[var] = find_parent(arr[var])
    return arr[var]


node.sort(key=lambda i: i[2])
result = 0
for a, b, c in node:
    a_n = find_parent(a)
    b_n = find_parent(b)
    if a_n != b_n:
        if a_n > b_n:
            arr[a_n] = b_n
        else:
            arr[b_n] = a_n
        result += c
print(result)
