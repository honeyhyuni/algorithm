# https://www.acmicpc.net/problem/1026
import sys
input = sys.stdin.readline

n = int(input())

a = list(map(int, input().split()))
b = list(map(int, input().split()))

result = 0
for i in range(n):
    a.sort()
    x = a[i]
    y = b.pop(b.index(max(b)))
    result += x * y
print(result)
