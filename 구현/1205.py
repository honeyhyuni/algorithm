# https://www.acmicpc.net/problem/1205
import sys

input = sys.stdin.readline
n, grade, p = map(int, input().split())
if n == 0:
    print(1)
else:
    arr = list(map(int, input().split()))
    if n == p and arr[-1] >= grade:
        print(-1)
    else:
        ans = n + 1
        for i in range(n):
            if arr[i] <= grade:
                ans = i+1
                break
        print(ans)
