# https://www.acmicpc.net/problem/2933
import sys
from collections import deque

input = sys.stdin.readline
n, m = map(int, input().split())
arr = [list(map(str, input().rstrip())) for i in range(n)]

T = int(input())
throw = list(map(int, input().split()))
dx, dy = [-1, 1, 0, 0], [0, 0, -1, 1]


def destroy(bol, x):
    x = n - x
    if bol:
        for i in range(m):
            if arr[x][i] == 'x':
                arr[x][i] = '.'
                check()
                return
    else:
        for i in range(m - 1, -1, -1):
            if arr[x][i] == 'x':
                arr[x][i] = '.'
                check()
                return


def check():
    visited = [[False] * m for i in range(n)]
    bol = False
    for i in range(n - 1, -1, -1):
        if bol:
            break
        for j in range(m):
            if bol:
                break
            if arr[i][j] == 'x' and not visited[i][j]:
                temp = []
                q = deque()
                q.append((i, j))
                visited[i][j] = True
                temp.append((i, j))
                while q:
                    x, y = q.popleft()
                    for _ in range(4):
                        nx = x + dx[_]
                        ny = y + dy[_]
                        if 0 <= nx < n and 0 <= ny < m and not visited[nx][ny] and arr[nx][ny] == 'x':
                            q.append((nx, ny))
                            temp.append((nx, ny))
                            visited[nx][ny] = True
                # x축을 밑에서 가까운 순으로 정렬후 떨어질수있는(분리된) 클라스크
                # 라면 떨어트림
                temp.sort(key=lambda x: (-x[0], x[1]))
                if temp[0][0] != n - 1:
                    # for 문을 나가기 위한 bol
                    bol = True
                    min_v = sys.maxsize
                    # 떨어진 얼음조각을 하나하나 확인하여
                    # 떨어질 위치의 최소값을 구해준다.
                    # 맨밑이거나 같은 얼음조각이 아닌 얼음 조각을 만났을때
                    # 위치 크기를 갱신해준다.
                    for _ in range(len(temp)):
                        x, y = temp[_][0], temp[_][1]
                        for nx in range(x, n):
                            if nx + 1 == n:
                                min_v = min(min_v, n - 1 - x)
                                break
                            elif arr[nx + 1][y] == 'x':
                                if (nx + 1, y) not in temp:
                                    min_v = min(min_v, nx - x)
                                    break
                    for x, y in temp:
                        arr[x][y] = '.'
                        arr[x + min_v][y] = 'x'


# 왼쪽 오른쪽 번갈아가면서 던짐
for i in range(T):
    if i % 2 == 0:
        destroy(True, throw[i])
    else:
        destroy(False, throw[i])
for i in arr:
    print("".join(i))
