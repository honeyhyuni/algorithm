# https://programmers.co.kr/learn/courses/30/lessons/43162
from collections import deque


def solution(n, computers):
    answer = 0
    visited = [False] * n
    q = deque()
    for i in range(n):
        if not visited[i]:
            answer += 1
            q.append(i)
            while q:
                visited[i] = True
                x = q.popleft()
                for _ in range(len(computers[x])):
                    if computers[x][_] == 1 and not visited[_]:
                        visited[_] = True
                        q.append(_)

    return answer
