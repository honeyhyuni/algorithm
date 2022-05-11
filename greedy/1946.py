# https://www.acmicpc.net/problem/1946
import sys
input = sys.stdin.readline
T = int(input())
for t in range(T):
    n = int(input())
    arr = []
    for i in range(n):
        arr.append(list(map(int, input().split())))
    arr.sort()
    max_v, cnt = arr[0][1], 1
    for i in range(1, n):
        if max_v == 1:
            break
        if max_v > arr[i][1]:
            cnt += 1
            max_v = arr[i][1]
    print(cnt)