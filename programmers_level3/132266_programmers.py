from collections import deque


def solution(n, roads, sources, destination):
    visited = [-1] * (n + 1)
    visited[destination] = 0
    arr = [[] for i in range(n + 1)]
    for i, j in roads:
        arr[i].append(j)
        arr[j].append(i)

    q = deque()
    q.append((destination, 1))

    while q:
        x, c = q.popleft()
        for i in arr[x]:
            if visited[i] == -1:
                visited[i] = c
                q.append((i, c + 1))

    return [visited[i] for i in sources]


print(solution(3, [[1, 2], [2, 3]], [2, 3], 1))
