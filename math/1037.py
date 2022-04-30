# https://www.acmicpc.net/problem/1037
n = int(input())
arr = list(map(int, input().split()))

print(arr[0]**2 if n == 1 else min(arr) * max(arr))
