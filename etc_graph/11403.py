# https://www.acmicpc.net/problem/11403
# 플로이드 - 와샬 이론 문제
n = int(input())
arr = []
for i in range(n):
    arr.append(list(map(int, input().split())))

for k in range(n):
    for a in range(n):
        for b in range(n):
            if arr[a][b] == 1 or (arr[a][k] == 1 and arr[k][b] == 1):
                arr[a][b] = 1

for i in range(n):
    for j in range(n):
        print(arr[i][j], end=' ')
    print()