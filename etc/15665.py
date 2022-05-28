# https://www.acmicpc.net/problem/15665
import sys

input = sys.stdin.readline
n, m = map(int, input().split())
arr = list(set(map(int, input().split())))

result = []


def back():
    if len(result) == m:
        print(*result)
        return
    for i in sorted(arr):
        result.append(i)
        back()
        result.pop()


back()
