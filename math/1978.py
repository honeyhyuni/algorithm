# https://www.acmicpc.net/problem/1978
import sys
input = sys.stdin.readline
n = int(input())
arr = list(map(int, input().split()))
result = 0
for i in arr:
    if i == 1:
        continue
    for j in range(2, int(i**0.5)+1):
        if i % j == 0:
            break
    else:
        result += 1

print(result)