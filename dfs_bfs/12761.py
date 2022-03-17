# https://www.acmicpc.net/problem/12761
from collections import deque
a, b, n, m = map(int, input().split())
arr = [0] * 100001
q = deque()
q.append(n)
while q:
    x = q.popleft()
    if x == m:
        print(arr[m])
        break
    for nx in [x-1, x+1, x-a, x+a, x-b, x+b, x*a, x*b]:
        if 0 <= nx < 100001 and arr[nx] == 0:
            arr[nx] = arr[x] + 1
            q.append(nx)
