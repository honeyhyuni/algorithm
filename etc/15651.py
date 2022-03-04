# https://www.acmicpc.net/problem/15651
import sys

input = sys.stdin.readline
n, m = map(int, input().split())
arr = []


def back():
    if len(arr) == m:
        print(' '.join(map(str, arr)))
        return
    for i in range(1, n + 1):
        arr.append(i)
        back()
        arr.pop()


back()