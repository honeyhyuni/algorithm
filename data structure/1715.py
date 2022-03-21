# https://www.acmicpc.net/problem/1715
import heapq

n = int(input())
heap = []
for i in range(n):
    heap.append(int(input()))

heapq.heapify(heap)
result = 0
while len(heap) != 1:
    num1 = heapq.heappop(heap)
    num2 = heapq.heappop(heap)
    sum_v = num1 + num2
    result += sum_v
    heapq.heappush(heap, sum_v)
print(result)