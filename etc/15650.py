# https://www.acmicpc.net/problem/15650
import sys

input = sys.stdin.readline
n, m = map(int, input().split())
arr = []


def back(start):
    if len(arr) == m:
        print(' '.join(map(str, arr)))
        return
    for i in range(start, n + 1):
        if i not in arr:
            arr.append(i)
            back(i+1)
            arr.pop()


back(1)
