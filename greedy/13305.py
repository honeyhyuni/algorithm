# https://www.acmicpc.net/problem/13305
import sys
input = sys.stdin.readline
n = int(input())
distance = list(map(int, input().split()))
arr = list(map(int, input().split()))

min_v = arr[0]

total = 0
for i in range(len(distance)):
    if arr[i] >= min_v:
        total += min_v * distance[i]
    elif arr[i] < min_v:
        min_v = arr[i]
        total += min_v * distance[i]
print(total)