# https://www.acmicpc.net/problem/15666
import sys

input = sys.stdin.readline
n, m = map(int, input().split())
arr = sorted(list(set(map(int, input().split()))))
n = len(arr)

result = []


def back(cnt):
    if len(result) == m:
        print(*result)
        return
    for i in range(cnt, n):
        result.append(arr[i])
        back(i)
        result.pop()


back(0)
