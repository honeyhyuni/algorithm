# https://www.acmicpc.net/problem/16435
n, l = map(int, input().split())

arr = list(map(int, input().split()))
arr.sort()
for i in range(n):
    if l >= arr[i]:
        l += 1
print(l)