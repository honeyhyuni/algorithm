# https://www.acmicpc.net/problem/13458
import sys
input = sys.stdin.readline
n = int(input())
arr = list(map(int, input().split()))
b, c = map(int, input().split())
result = n
for i in range(n):
    arr[i] -= b
    if arr[i] <= 0:
        continue
    v, mod = divmod(arr[i], c)
    if mod > 0:
        result += v + 1
    else:
        result += v
print(result)