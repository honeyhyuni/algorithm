# https://www.acmicpc.net/problem/2887
import sys

input = sys.stdin.readline
n = int(input())

xlst, ylst, zlst = [], [], []
for i in range(n):
    x, y, z = map(int, input().split())
    xlst.append((x, i))
    ylst.append((y, i))
    zlst.append((z, i))
xlst.sort()
ylst.sort()
zlst.sort()
node = []
parent = [i for i in range(n)]

for xyz in xlst, ylst, zlst:
    for i in range(1, n):
        node.append((abs(xyz[i-1][0] - xyz[i][0]), xyz[i-1][1], xyz[i][1]))


def find_parent(var):
    if var != parent[var]:
        parent[var] = find_parent(parent[var])
    return parent[var]


result = 0


cnt = 0
for v, a, b in sorted(node):
    if cnt == n - 1:
        break
    a_n, b_n = find_parent(a), find_parent(b)
    if a_n != b_n:
        if a_n < b_n:
            parent[b_n] = a_n
        else:
            parent[a_n] = b_n
        cnt += 1
        result += v

print(result)
