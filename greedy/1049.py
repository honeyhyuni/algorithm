# https://www.acmicpc.net/problem/1049
import sys
input = sys.stdin.readline
n, m = map(int, input().split())

minset = sys.maxsize
minnotset = sys.maxsize

result = sys.maxsize
for i in range(m):
    x, y = map(int, input().split())
    minset = min(minset, x)
    minnotset = min(minnotset, y)

cnt = n // 6 + 1
min_v = sys.maxsize
for i in range(cnt + 1):
    result = 0
    temp = n
    temp -= i * 6
    result += i * minset
    if temp > 0:
        result += temp * minnotset
    min_v = min(min_v, result)
print(min_v)