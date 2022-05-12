# https://www.acmicpc.net/problem/19598
import sys
from heapq import heappop, heappush
input = sys.stdin.readline
n = int(input())
arr = []
for i in range(n):
    arr.append(list(map(int, input().split())))
arr.sort()
class_room = [arr.pop(0)[1]]
for start, end in arr:
    if start < class_room[0]:
        heappush(class_room, end)
    else:
        heappop(class_room)
        heappush(class_room, end)
print(len(class_room))
