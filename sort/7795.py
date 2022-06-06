# https://www.acmicpc.net/problem/7795
import sys

input = sys.stdin.readline
T = int(input())


def binary_search(value, start, end):
    result = -1
    while start <= end:
        mid = (start + end) // 2
        if B[mid] < value:
            result = mid
            start = mid + 1
        else:
            end = mid - 1
    return result


for t in range(T):
    n, m = map(int, input().split())
    A = list(map(int, input().split()))
    B = sorted(list(map(int, input().split())))
    cnt = 0
    for a in A:
        start, end = 0, m - 1
        cnt += binary_search(a, start, end) + 1
    print(cnt)
