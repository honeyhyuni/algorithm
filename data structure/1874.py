# https://www.acmicpc.net/problem/1874
import sys

n = int(input())
cnt = 1
arr = []
op = []

for i in range(n):
    x = int(input())
    while cnt <= x:
        arr.append(cnt)
        op.append("+")
        cnt += 1
    if arr[-1] == x:
        arr.pop()
        op.append("-")
    else:
        print("NO")
        sys.exit()

print("\n".join(op))