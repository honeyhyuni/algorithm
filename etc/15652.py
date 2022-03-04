# https://www.acmicpc.net/problem/15652
import sys

input = sys.stdin.readline
n, m = map(int, input().split())
arr = []


def back(st):
    if len(arr) == m:
        print(*arr)
        return
    for i in range(st, n + 1):
        arr.append(i)
        back(i)
        arr.pop()


back(1)
