# https://www.acmicpc.net/problem/17281
from itertools import permutations
import sys
input = sys.stdin.readline

n = int(input())
arr = []
for i in range(n):
    arr.append(list(map(int, input().split())))
max_v = -1
lst = [1, 2, 3, 4, 5, 6, 7, 8]
per = list(permutations(lst))

for i in per:
    p = list(i[:3]) + [0] + list(i[3:])
    y = 0
    score = 0
    for x in range(n):
        out = 0
        b1, b2, b3 = 0, 0, 0
        while out < 3:
            if arr[x][p[y]] == 0:
                out += 1
            elif arr[x][p[y]] == 1:
                score += b3
                b1, b2, b3 = 1, b1, b2
            elif arr[x][p[y]] == 2:
                score += b3 + b2
                b1, b2, b3 = 0, 1, b1
            elif arr[x][p[y]] == 3:
                score += b1 + b2 + b3
                b1, b2, b3 = 0, 0, 1
            else:
                score += b1 + b2 + b3 + 1
                b1, b2, b3 = 0, 0, 0
            y = (y+1) % 9
    max_v = max(max_v, score)
print(max_v)


# 시간초과
# for _ in per:
#     _ = list(_[:3]) + [0] + list(_[3:])
#     stack = []
#     x, y = 0, 0
#     out = 0
#     jumsu = 0
#     while x < n:
#         if arr[x][_[y]] == 0:
#             out += 1
#         elif 1 <= arr[x][_[y]] <= 3:
#             if not stack:
#                 stack.append(arr[x][_[y]])
#             else:
#                 for i in range(len(stack)):
#                     stack[i] += arr[x][_[y]]
#                     if stack[i] >= 4:
#                         stack[i] = 4
#                 while 4 in stack:
#                     stack.remove(4)
#                     jumsu += 1
#                 stack.append(arr[x][_[y]])
#         else:
#             jumsu += len(stack) + 1
#             stack.clear()
#         y = (y + 1) % 9
#         if out == 3:
#             stack.clear()
#             x += 1
#             out = 0
#     max_v = max(max_v, jumsu)
# print(max_v)

