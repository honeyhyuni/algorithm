# https://www.acmicpc.net/problem/1043
from collections import deque
import sys

input = sys.stdin.readline
n, m = map(int, input().split())

# bfs 풀이
# arr = []
# liar = list(map(int, input().split()))
# dp = [[] for i in range(n+1)]
# visited = [False] * (n+1)
# for i in range(m):
#     temp = list(map(int, input().split()))
#     arr.append(temp)
#     for j in range(temp[0]):
#         dp[temp[j+1]].extend(temp[1:])
# 
# for i in liar[1:]:
#     if not visited[i]:
#         q = deque()
#         q.append(i)
#         visited[i] = True
#         while q:
#             x = q.popleft()
#             for _ in dp[x]:
#                 if not visited[_]:
#                     visited[_] = True
#                     q.append(_)
# cnt = 0
# for i in arr:
#     for j in i[1:]:
#         if visited[j]:
#             break
#     else:
#         cnt += 1
# print(cnt)

# set 자료구조 사용
liar = set(input().split()[1:])
arr = []
for i in range(m):
    arr.append(set(input().split()[1:]))

for _ in range(m):
    for i in arr:
        if i & liar:
            liar |= i

for i in arr:
    if i & liar:
        m -= 1
print(m)
