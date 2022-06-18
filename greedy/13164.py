# https://www.acmicpc.net/problem/13164
import sys
input = sys.stdin.readline

n, k = map(int, input().split())
arr = list(map(int, input().split()))

result = []

for i in range(n-1):
    result.append(arr[i+1] - arr[i])

result.sort()

print(sum(result[:n-k]))