# https://www.acmicpc.net/problem/1253
import sys
input = sys.stdin.readline
n = int(input())
arr = sorted(list(map(int, input().split())))


def b_search(a, target):
    start, end = 0, n - 2
    while start < end:
        temp = a[start] + a[end]
        if temp == target:
            return 1
        elif temp < target:
            start += 1
        else:
            end -= 1
    return 0


result = 0
for i in range(n):
    result += b_search(arr[:i] + arr[i + 1:], arr[i])
print(result)
