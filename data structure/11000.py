# https://www.acmicpc.net/problem/11000
import sys
import heapq
n = int(sys.stdin.readline())

arr = []
for i in range(n):
    a, b = map(int, sys.stdin.readline().split())
    arr.append((a, b))

arr.sort(key= lambda x : (x[0], x[1]))

room = []

heapq.heappush(room, arr[0][1])

for i in range(1, n):
    if arr[i][0] < room[0]:
        heapq.heappush(room, arr[i][1])

    else:
        heapq.heappop(room)
        heapq.heappush(room, arr[i][1])
print(len(room))



