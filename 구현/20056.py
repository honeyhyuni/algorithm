# https://www.acmicpc.net/problem/20056
import sys

input = sys.stdin.readline

dx, dy = [-1, -1, 0, 1, 1, 1, 0, -1], [0, 1, 1, 1, 0, -1, -1, -1]

n, m, k = map(int, input().split())
arr = [[[] for i in range(n)] for i in range(n)]

fireball = []
for i in range(m):
    x, y, m, s, d = map(int, input().split())
    fireball.append((x - 1, y - 1, m, s, d))

for ii in range(k):

    while fireball:
        x, y, m, s, d = fireball.pop(0)
        nx = (x + dx[d] * s) % n
        ny = (y + dy[d] * s) % n
        arr[nx][ny].append((m, s, d))

    for i in range(n):
        for j in range(n):
            if len(arr[i][j]) >= 2:
                m_v, s_v, odd, even = 0, 0, 0, 0
                len_ = len(arr[i][j])

                while arr[i][j]:
                    m, s, d = arr[i][j].pop()
                    m_v += m
                    s_v += s
                    if d % 2:
                        odd += 1
                    else:
                        even +=1
                if m_v // 5 == 0:
                    continue
                if odd == len_ or even == len_:
                    t = [0, 2, 4, 6]
                else:
                    t = [1, 3, 5, 7]
                for nd in t:
                    fireball.append((i, j, m_v // 5, s_v // len_, nd))
            elif len(arr[i][j]) == 1:
                m, s, d = arr[i][j].pop()
                fireball.append((i, j, m, s, d))

print(sum(i[2] for i in fireball))
