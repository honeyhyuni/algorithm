# https://www.acmicpc.net/problem/11866
import collections
n, k = map(int, input().split())

a = collections.deque([i for i in range(1, n+1)])
b = []
while a:
    a.rotate(-(k-1))
    b.append(a.popleft())

print("<", end='')

for i in range(n):
    if i == n-1:
        print("%d>" %(b[i]))
    else:
        print("%d," % (b[i]), end=' ')

