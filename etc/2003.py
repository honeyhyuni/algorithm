# https://www.acmicpc.net/problem/2003
import sys
input = sys.stdin.readline
n, m = map(int, input().split())
arr = list(map(int, input().split()))
result = 0
left, right = 0, 1

while right <= n:
    sum_v = sum(arr[left:right])
    if sum_v == m:
        result += 1
    if sum_v >= m:
        left += 1
    else:
        right += 1
print(result)