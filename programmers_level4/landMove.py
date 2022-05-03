# https://programmers.co.kr/learn/courses/30/lessons/62050
from collections import deque


def solution(land, height):
    answer = 0
    dx = [-1, 1, 0, 0]
    dy = [0, 0, -1, 1]
    n, m = len(land), len(land[0])
    cnt = 1
    visited = [[0] * m for i in range(n)]
    node = []
    # 서로 연결될수 있는 지형은 같은 숫자로 visited 배열에 저장 -> 한노드로 표현
    for i in range(n):
        for j in range(m):
            if visited[i][j] == 0:
                visited[i][j] = cnt
                q = deque()
                q.append([i, j])
                while q:
                    x, y = q.popleft()
                    for _ in range(4):
                        nx = x + dx[_]
                        ny = y + dy[_]
                        if 0 <= nx < n and 0 <= ny < m:
                            if visited[nx][ny] == 0:
                                if abs(land[nx][ny] - land[x][y]) <= height:
                                    visited[nx][ny] = cnt
                                    q.append([nx, ny])
                            # 최소 신장 트리 구현을 위한 각 노드의 번호와 거리를 node 배열에 저장
                            if visited[nx][ny] != 0:
                                if visited[nx][ny] != visited[x][y]:
                                    node.append([visited[x][y], visited[nx][ny], abs(land[nx][ny] - land[x][y])])

                cnt += 1
    # 크루스칼
    arr = [i for i in range(cnt)]

    def find_parent(var):
        if var != arr[var]:
            arr[var] = find_parent(arr[var])
        return arr[var]

    node.sort(key=lambda x: x[2])

    for a, b, c in node:
        a_n = find_parent(a)
        b_n = find_parent(b)
        if a_n != b_n:
            if a_n < b_n:
                arr[b_n] = a_n
            else:
                arr[a_n] = b_n
            answer += c
    return answer


print(solution([[1, 4, 8, 10], [5, 5, 5, 5], [10, 10, 10, 10], [10, 10, 10, 20]], 3))
print(solution([[10, 11, 10, 11], [2, 21, 20, 10], [1, 20, 21, 11], [2, 1, 2, 1]], 1))
