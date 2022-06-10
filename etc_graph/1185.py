# https://www.acmicpc.net/problem/1185
import sys

input = sys.stdin.readline
n, m = map(int, input().split())
land_cost = [0] + [int(input()) for i in range(n)]  # 나라 비용

parent = [i for i in range(n + 1)]
node = []


def find_parent(var):
    if var != parent[var]:
        parent[var] = find_parent(parent[var])
    return parent[var]


# (land_cost[a] + land_cost[b]) + (c * 2)) -> 시작 나라에서 결국 도착지점은 시작 나라
# 스패닝 으로 다 연결 시켜 논뒤 제일 적은 비용의 나라를 더하면 끝.
for i in range(m):
    a, b, c = map(int, input().split())
    node.append((((land_cost[a] + land_cost[b]) + (c * 2)), a, b))
node.sort()
result = 0
for c, a, b in node:
    a_n, b_n = find_parent(a), find_parent(b)
    if a_n != b_n:
        if a_n < b_n:
            parent[b_n] = a_n
        else:
            parent[a_n] = b_n
        result += c

print(result + min(land_cost[1:]))
