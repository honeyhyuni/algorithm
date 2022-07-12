# https://www.acmicpc.net/problem/14226
from collections import deque
S = int(input())

q = deque()
q.append((1, 0))
visited = {(1, 0): 0}

while q:
    now, clip = q.popleft()
    if now == S:
        print(visited[(now, clip)])
        break
    for n_n, n_c in [(now, now), (now+clip, clip), (now-1, clip)]:
        if (n_n, n_c) not in visited:
            visited[(n_n, n_c)] = visited[(now, clip)] + 1
            q.append((n_n, n_c))
