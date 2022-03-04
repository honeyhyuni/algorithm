# https://www.acmicpc.net/problem/15649
# 백트래킹 기본 문제
import sys

input = sys.stdin.readline
n, m = map(int, input().split())

arr = []


def back():
    if len(arr) == m:
        print(' '.join(map(str, arr)))
        return

    for i in range(1, n + 1):
        if i not in arr:
            arr.append(i)
            back()
            arr.pop()


back()
