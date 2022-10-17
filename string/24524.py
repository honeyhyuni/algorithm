# https://www.acmicpc.net/problem/24524
import sys
input = sys.stdin.readline
a = input().rstrip()
b = input().rstrip()
visited = [0] * len(b)
for i in range(len(a)):
    for j in range(len(b)):
        if a[i] == b[j]:
            if j == 0:
                visited[0] += 1
            elif visited[j] < visited[j-1]:
                visited[j] += 1
print(visited[-1])