# https://www.acmicpc.net/problem/4386
import math
import sys

input = sys.stdin.readline
n = int(input())
arr = [i for i in range(n)]
temp = []
for i in range(n):
    x, y = map(float, input().split())
    temp.append([x, y])
node = []
for i in range(len(temp)):
    for j in range(i + 1, len(temp)):
        node.append([i, j, math.sqrt((temp[j][0] - temp[i][0]) ** 2 + ((temp[j][1]) - temp[i][1]) ** 2)])
        node.append([j, i, math.sqrt((temp[j][0] - temp[i][0]) ** 2 + ((temp[j][1]) - temp[i][1]) ** 2)])

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
