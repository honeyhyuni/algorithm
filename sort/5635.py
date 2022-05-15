# https://www.acmicpc.net/problem/5635
import sys
input = sys.stdin.readline
n = int(input())
arr = [list(map(str, input().split())) for i in range(n)]
arr.sort(key= lambda x: (int(x[3]), int(x[2]), int(x[1])))

print(arr[-1][0])
print(arr[0][0])