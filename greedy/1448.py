# https://www.acmicpc.net/problem/1448
n = int(input())

arr = []
for i in range(n):
    a = int(input())
    arr.append(a)

arr.sort()
result = -1
for i in range(n - 2):
    if arr[i] + arr[i + 1] > arr[i + 2]:
        result = max(result, arr[i] + arr[i + 1] + arr[i + 2])
print(result)
