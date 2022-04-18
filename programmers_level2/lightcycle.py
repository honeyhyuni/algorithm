# https://programmers.co.kr/learn/courses/30/lessons/86052/solution_groups?language=python3
dx = [1, 0, -1, 0]
dy = [0, 1, 0, -1]


def solution(grid):
    global visited, n, m
    answer = []

    n, m = len(grid), len(grid[0])
    visited = [[[False] * 4 for i in range(m)] for i in range(n)]
    for i in range(n):
        for j in range(m):
            for k in range(4):
                if not visited[i][j][k]:
                    cmd = light(i, j, k, grid)
                    if cmd:
                        answer.append(cmd)

    return sorted(answer)

def light(sx, sy, sd, grid):
    global visited
    visited[sx][sy][sd] = True
    x, y, d = sx, sy, sd
    cnt = 0
    while True:
        x = (x + dx[d]) % n
        y = (y + dy[d]) % m
        cnt += 1

        if grid[x][y] == "R":
            d = (d+1) % 4
        elif grid[x][y] == "L":
            d = (d-1) % 4
        if visited[x][y][d]:
            if (x, y, d) == (sx, sy, sd):
                return cnt
            else:
                return 0
        visited[x][y][d] = True



print(solution(["SL","LR"]))
print(solution(["S"]))
print(solution(["R","R"]))