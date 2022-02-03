# https://www.acmicpc.net/problem/15903
import sys
input = sys.stdin.readline

n, m = map(int, input().split())
arr = list(map(int, input().split()))
result = 0
for i in range(m):
    arr.sort()
    result = arr[0] + arr[1]
    arr[0], arr[1] = result, result
print(sum(arr))
