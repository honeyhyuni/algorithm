# https://www.acmicpc.net/problem/11399
n = int(input())
p = list(map(int, input().split()))

sum = 0
p.sort()
for i in range(n):
    for j in range(i + 1):
        sum += p[j]

print(sum)