# https://www.acmicpc.net/problem/23351
n, k, a, b = map(int, input().split())

arr = [k] * n
cnt = 0
while True:
    arr.sort()
    for i in range(a):
        arr[i] = arr[i] + b
    for i in range(n):
        arr[i] = arr[i] - 1
    if 0 in arr:
        break
    cnt += 1
print(cnt + 1)