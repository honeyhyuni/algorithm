# 에드몬드-카프 알고리즘
# 최대 유량, 네트워크 플로우 알고리즘
# https://www.acmicpc.net/problem/6086
import sys
from collections import deque

input = sys.stdin.readline
INF = sys.maxsize


def change_Num(v):
    if ord(v) <= 90:
        return ord(v) - 65
    elif ord(v) <= 122:
        return ord(v) - 97 + 26


# source - sink 최소 flow 구해줌
def find_MinValue(node):
    global min_v
    if node == 0:
        return
    temp = capacity[prev[node]][node] - flow[prev[node]][node]
    if temp < min_v:
        min_v = temp
    find_MinValue(prev[node])


# source - sink 최소 flow 더해줌
def make_Flow(min_v, node):
    if node == 0:
        return
    flow[prev[node]][node] += min_v
    flow[node][prev[node]] -= min_v
    make_Flow(min_v, prev[node])


n = int(input())
capacity = [[0] * 52 for i in range(52)]
flow = [[0] * 52 for i in range(52)]
for i in range(n):
    o, t, c = input().split()
    o_v = change_Num(o)
    t_v = change_Num(t)
    c = int(c)
    capacity[o_v][t_v] += c
    capacity[t_v][o_v] += c

goal = change_Num("Z")
result = 0

while True:
    q = deque()
    q.append(0)
    prev = [-1] * 52
    while q:
        now = q.popleft()
        for n_n in range(52):
            if capacity[now][n_n] - flow[now][n_n] > 0 and prev[n_n] == -1:
                prev[n_n] = now
                q.append(n_n)
    if prev[goal] == -1:
        break
    min_v = INF
    find_MinValue(goal)
    make_Flow(min_v, goal)
    result += min_v

print(result)
