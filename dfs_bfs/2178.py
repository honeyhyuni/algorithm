# https://www.acmicpc.net/problem/2178
x1 = [-1, 1, 0, 0]
y1 = [0, 0, -1, 1]

n, m = map(int, input().split())
arr = []
for _ in range(n):
    arr.append(list(map(int, input())))

q = [[0, 0]]
arr[0][0] = 1
while q:
    x, y = q[0][0], q[0][1]
    del q[0]
    for i in range(4):
        nx = x + x1[i]
        ny = y + y1[i]
        if 0 <= nx < n and 0 <= ny < m and arr[nx][ny] == 1:
            q.append([nx, ny])
            arr[nx][ny] = arr[x][y] + 1 # 1을 만날때마다 1씩 증가
print(arr[n-1][m-1])
