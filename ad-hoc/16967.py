# https://www.acmicpc.net/problem/16967
import sys
input = sys.stdin.readline
n, m, pn, pm = map(int, input().split())
b = [list(map(int, input().split())) for i in range(n+pn)]
for i in range(pn, n):
    for j in range(pm, m):
        b[i][j] -= b[i-pn][j-pm]

for i in range(n):
    print(*b[i][:m])