# https://www.acmicpc.net/problem/11047
n, k = map(int, input().split())

a = []
sum = 0
for i in range(n):
    a.append(int(input()))
for i in range(n-1, -1, -1):
    if k == 0:
        break
    if a[i] > k:
        continue
    sum += k // a[i]
    k %= a[i]

print(sum)


