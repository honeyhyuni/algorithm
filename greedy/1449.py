# https://www.acmicpc.net/problem/1449
n, l = map(int, input().split())

a = list(map(int, input().split()))
a.sort()
count = 0

k = -2

for i in range(n):
    if a[i] > k:
        k = a[i] + l-1
        count += 1
print(count)



