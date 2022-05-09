# https://www.acmicpc.net/problem/11967
from collections import deque
import sys
from collections import defaultdict

input = sys.stdin.readline
n, m = map(int, input().split())
dic = defaultdict(set)
dx = [-1, 0, 1, 0]
dy = [0, -1, 0, 1]
for i in range(m):
    x, y, a, b = map(int, input().split())
    dic[x-1, y-1].add((a-1, b-1))
arr = [[0] * n for i in range(n)]
visited = [[False] * n for i in range(n)]
q = deque()
q.append([0, 0])
arr[0][0] = 1
visited[0][0] = True
while q:
    x, y = q.popleft()
    # 스위치가 연결되어 있는곳의 전원을 모두킴
    if (x, y) in dic.keys():
        for j in dic[x, y]:
            arr[j[0]][j[1]] = 1
            # 불이 켜졌고 방문하지 않았던 곳의
            # 주변이 불이 켜져있고 방문했던 곳이면 큐에 추가
            if not visited[j[0]][j[1]]:
                for _ in range(4):
                    nx = j[0] + dx[_]
                    ny = j[1] + dy[_]
                    if 0 <= nx < n and 0 <= ny < n:
                        if arr[nx][ny] == 1 and visited[nx][ny]:
                            q.append([j[0], j[1]])
                            visited[j[0]][j[1]] = True
                            break
    for _ in range(4):
        nx = x + dx[_]
        ny = y + dy[_]
        if 0 <= nx < n and 0 <= ny < n:
            # 방문한적없고 불이 켜져있으면 큐에 추가
            if not visited[nx][ny] and arr[nx][ny] == 1:
                q.append([nx, ny])
                visited[nx][ny] = True

result = 0
for i in arr:
    result += i.count(1)
print(result)