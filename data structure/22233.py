# https://www.acmicpc.net/problem/22233
import sys
input = sys.stdin.readline
n, m = map(int, input().split())

s = set()
for i in range(n):
    s.add(input().rstrip())
result = n
for i in range(m):
    t = input().rstrip().split(",")
    for j in t:
        try:
            s.remove(j)
            result -=1
        except:
            continue
    print(result)