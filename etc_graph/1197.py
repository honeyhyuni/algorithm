# https://www.acmicpc.net/problem/1197
# 크루스칼 기본 이론문제
import sys

input = sys.stdin.readline
v, e = map(int, input().split())

arr = [i for i in range(v + 1)]
node = []
for i in range(e):
    x, y, z = map(int, input().split())
    node.append([x, y, z])
    node.append([y, x, z])

node.sort(key=lambda i: i[2])


def find_parent(var):
    if var != arr[var]:
        arr[var] = find_parent(arr[var])
    return arr[var]


# def union_node(a, b):
#     a_n = find_parent(a)
#     b_n = find_parent(b)
#     if a_n > b_n:
#         arr[a_n] = b_n
#     else:
#         arr[b_n] = a_n


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
