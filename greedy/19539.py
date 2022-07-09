# https://www.acmicpc.net/problem/19539
import sys
input = sys.stdin.readline
n = int(input())
arr = list(map(int, input().split()))
sum_v = sum(arr)
total = sum(arr) % 3
if total == 0:
    cnt = 0
    for i in arr:
        cnt += i // 2
    if cnt >= sum_v//3:
        print("YES")
    else:
        print("NO")
else:
    print("NO")