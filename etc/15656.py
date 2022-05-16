# https://www.acmicpc.net/problem/15656
import sys

input = sys.stdin.readline
n, m = map(int, input().split())
arr = sorted(list(map(int, input().split())))
result = []


def back():
    if len(result) == m:
        print(" ".join(map(str, result)))
        return
    for i in arr:
        result.append(i)
        back()
        result.pop()


back()
