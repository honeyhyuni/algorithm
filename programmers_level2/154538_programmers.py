# https://school.programmers.co.kr/learn/courses/30/lessons/154538
from collections import deque


def solution(x, y, n):
    max_ = 1000001
    visited = [False] * max_
    q = deque()
    q.append((x, 0))
    while q:
        t, c = q.popleft()
        if t == y:
            return c
        for i in [t+n, t*2, t*3]:
            if i < max_ and not visited[i]:
                visited[i] = True
                q.append((i, c+1))
    return -1


print(solution(10, 40, 5))
print(solution(10, 40, 30))
print(solution(2, 5, 4))
