# https://www.acmicpc.net/problem/1080
def change(x, y): # 1 -> 0, 0 -> 1
    for i in range(x, x + 3):
        for j in range(y, y + 3):
            A[i][j] = 1 - A[i][j]


n, m = map(int, input().split())
A, B = [], []
for i in range(n):
    A.append(list(map(int, input())))
for i in range(n):
    B.append(list(map(int, input())))

cnt = 0
for i in range(n - 2):
    for j in range(m - 2):
        if A[i][j] != B[i][j]:
            change(i, j)
            cnt += 1
for i in range(n): # 하나라도 다를시 -1 출력
    for j in range(m):
        if A[i][j] != B[i][j]:
            cnt = -1
print(cnt)
