# https://www.acmicpc.net/problem/2842
import sys
from collections import deque

input = sys.stdin.readline

dx, dy = [-1, -1, -1, 0, 1, 1, 1, 0], [-1, 0, 1, 1, 1, 0, -1, -1]


def bfs(l, r):
    q = deque()
    if l <= fatigue[sx][sy] <= r:
        q.append((sx, sy))
    t = K_
    visited = [[False] * n for i in range(n)]
    visited[sx][sy] = True
    while q:
        x, y = q.popleft()
        for _ in range(8):
            nx = x + dx[_]
            ny = y + dy[_]
            if 0 <= nx < n and 0 <= ny < n and not visited[nx][ny]:
                if l <= fatigue[nx][ny] <= r:
                    if city[nx][ny] == "K":
                        t -= 1
                    q.append((nx, ny))
                    visited[nx][ny] = True
    if t == 0:
        return True
    return False


n = int(input())
city = [list(map(str, input().rstrip())) for i in range(n)]
fatigue = [list(map(int, input().split())) for i in range(n)]
K_ = 0
num = set()

for i in range(n):
    for j in range(n):
        if city[i][j] == 'P':
            sx, sy = i, j
        elif city[i][j] == 'K':
            K_ += 1
        num.add(fatigue[i][j])

# 최대 최소 만 구하면됨으로 set으로 처리
num = sorted(list(num))

ans = sys.maxsize

# 투포인터 로 최솟값 <= 피로도 <= 최대값 을 확인하고 
# bfs 함수에서 return True 라면 ans 값 갱신
left, right = 0, num.index(fatigue[sx][sy])
while left < len(num):
    l, r = num[left], num[right]
    bol = bfs(l, r)
    if bol:
        left += 1
        ans = min(ans, r - l)
    else:
        if right + 1 < len(num):
            right += 1
        else:
            break
print(ans)
