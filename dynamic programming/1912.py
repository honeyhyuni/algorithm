# https://www.acmicpc.net/problem/1912
import sys
input = sys.stdin.readline
n = int(input())
arr = list(map(int, input().split()))

sum = [arr[0]]
for i in range(len(arr) -1):
    sum.append(max(sum[i] + arr[i + 1], arr[i + 1]))
print(max(sum))