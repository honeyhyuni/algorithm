# https://www.acmicpc.net/problem/25498
import sys
from collections import deque
input = sys.stdin.readline
n = int(input())
arr = [[] for i in range(n)]
st = input().rstrip()
for i in range(n-1):
    a, b = map(int, input().split())
    arr[a-1].append(b-1)
    arr[b-1].append(a-1)

q = deque()
q.append(0)
visited = [False] * n
visited[0] = True
result = st[0]

while q:
    min_v = 'A'
    temp = []
    for _ in range(len(q)):
        x = q.popleft()
        for i in arr[x]:
            if not visited[i]:
                visited[i] = True
                if st[i] > min_v:
                    min_v = st[i]
                    temp = [i]
                elif st[i] == min_v:
                    temp.append(i)
    q = deque(temp)
    if min_v != 'A':
        result += min_v

print(result)