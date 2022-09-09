# https://www.acmicpc.net/problem/1379
import sys
from heapq import heappop, heappush
input = sys.stdin.readline
n = int(input())
arr = [list(map(int, input().split())) for i in range(n)]
result = [0] * (n+1)
arr.sort(key= lambda x: x[1])
heap = []
grade = 0
while arr:
    v, s, e = arr.pop(0)
    if heap and heap[0][0] <= s:
        x, y = heappop(heap)
        result[v] = result[y]
    else:
        grade += 1
        result[v] = grade
    heappush(heap, [e, v])
print(grade)
print("\n".join(map(str, result[1:])))