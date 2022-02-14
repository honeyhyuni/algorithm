# https://www.acmicpc.net/problem/3135
a, b = map(int, input().split())
n = int(input())

arr = []
for i in range(n):
    arr.append(int(input()))

result = abs(b - a)
for i in range(n):
    arr[i] = abs(b - arr[i])

result2 = min(arr) + 1

print(min(result, result2))
