# https://www.acmicpc.net/problem/16398
import sys

input = sys.stdin.readline
n = int(input())
temp, node = [], []
for i in range(n):
    temp.append(list(map(int, input().split())))
for i in range(n):
    for j in range(n):
        if temp[i][j]:
            node.append([i, j, temp[i][j]])
arr = [i for i in range(n)]
node.sort(key=lambda x: x[2])


def find_parent(var):
    if var != arr[var]:
        arr[var] = find_parent(arr[var])
    return arr[var]


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
