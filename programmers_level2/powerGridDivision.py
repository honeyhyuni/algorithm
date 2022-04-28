# https://programmers.co.kr/learn/courses/30/lessons/86971
import sys
from collections import deque


def solution(n, wires):
    answer = sys.maxsize
    arr = [[] for i in range(n + 1)]
    for i, j in wires:
        arr[i].append(j)
        arr[j].append(i)
    for i, j in wires:
        visited = [False] * (n + 1)
        visited[i] = True
        visited[j] = True
        q = deque()
        q.append(i)
        while q:
            x = q.popleft()
            for _ in arr[x]:
                if not visited[_]:
                    visited[_] = True
                    q.append(_)
        temp = visited.count(True) - 1
        min_v = n - temp
        answer = min(answer, abs(min_v - temp))

    return answer


print(solution(9, [[1, 3], [2, 3], [3, 4], [4, 5], [4, 6], [4, 7], [7, 8], [7, 9]]))
print(solution(4, [[1, 2], [2, 3], [3, 4]]))
print(solution(7, [[1, 2], [2, 7], [3, 7], [3, 4], [4, 5], [6, 7]]))
