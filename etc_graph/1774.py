# https://www.acmicpc.net/problem/1774
import math
import sys


def find_parent(var):
    if var != arr[var]:
        arr[var] = find_parent(arr[var])
    return arr[var]


input = sys.stdin.readline
n, m = map(int, input().split())
arr = [i for i in range(n + 1)]
temp = [[]]
for i in range(n):
    x, y = map(int, input().split())
    temp.append([x, y])
for i in range(m):
    x, y = map(int, input().split())
    x_n = find_parent(x)
    y_n = find_parent(y)
    if x_n != y_n:
        if x_n < y_n:
            arr[y_n] = x_n
        else:
            arr[x_n] = y_n
node = []

for i in range(1, n + 1):
    for j in range(i + 1, n + 1):
        node.append([i, j, math.sqrt((temp[j][0] - temp[i][0]) ** 2 + (temp[j][1] - temp[i][1]) ** 2)])
        node.append([j, i, math.sqrt((temp[j][0] - temp[i][0]) ** 2 + (temp[j][1] - temp[i][1]) ** 2)])
node.sort(key=lambda x: x[2])

result = 0

for a, b, c in node:
    a_n = find_parent(a)
    b_n = find_parent(b)
    if a_n != b_n:
        if a_n < b_n:
            arr[b_n] = a_n
        else:
            arr[a_n] = b_n
        result += c

print('%.2f' % result)


