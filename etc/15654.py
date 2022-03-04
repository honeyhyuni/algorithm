# https://www.acmicpc.net/problem/15654
import sys
input = sys.stdin.readline
n, m = map(int, input().split())
arr = list(map(int, input().split()))
arr.sort()
back_arr = []
def back(arr):
    if len(back_arr) == m:
        print(*back_arr)
        return
    for i in arr:
        if i in back_arr:
            continue
        back_arr.append(i)
        back(arr)
        back_arr.pop()

back(arr)