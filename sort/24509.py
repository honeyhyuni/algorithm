# https://www.acmicpc.net/problem/24509
import sys
input = sys.stdin.readline
arr = []
result = []
n = int(input())
for i in range(n):
    arr.append(list(map(int, input().split())))
for i in range(1, 5):
    arr.sort(key= lambda x: (-x[i], x[0]))
    result.append(arr[0][0])
    arr.pop(0)

print(" ".join(map(str, result)))