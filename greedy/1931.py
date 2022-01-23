# https://www.acmicpc.net/problem/1931
import sys
n = int(sys.stdin.readline())
a = []
for _ in range(n):
    x, y = map(int, sys.stdin.readline().split())
    a.append((x, y))

a.sort(key= lambda x : (x[1], x[0]))

end = 0
cnt = 0

for i, j in a:
    if i >= end:
        cnt += 1
        end = j
print(cnt)
print(a)