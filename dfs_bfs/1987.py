# https://www.acmicpc.net/problem/1987
# deque 사용시 메모리초과
# set 자료구조 이용
import sys
dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]
input = sys.stdin.readline
n, m = map(int, input().split())
arr = []
for i in range(n):
    arr.append(list(map(str, input().rstrip())))
q = set()
q.add((0, 0, arr[0][0]))
max_v = 0
while q:
    x, y, temp = q.pop()
    for _ in range(4):
        nx = x + dx[_]
        ny = y + dy[_]
        if 0 <= nx < n and 0 <= ny < m and arr[nx][ny] not in temp:
            q.add((nx, ny, temp+arr[nx][ny]))
            max_v = max(max_v, len(temp))

print(max_v+1)