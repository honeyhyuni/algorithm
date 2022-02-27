# https://www.acmicpc.net/problem/11508
import sys
input = sys.stdin.readline
arr = []
n = int(input())
for i in range(n):
    arr.append(int(input()))
arr.sort(reverse=True)
result = 0
for i in range(n):
    if i % 3 != 2:
        result += arr[i]
print(result)