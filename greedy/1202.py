# https://www.acmicpc.net/problem/1202
import sys
from heapq import heappop, heappush
input = sys.stdin.readline
n, k = map(int, input().split())
jew = [tuple(map(int, input().split())) for i in range(n)]
bags = [int(input()) for i in range(k)]

jew.sort(reverse=True)
bags.sort()

heap, answer = [], 0
# 무게 상관없이 더작은 가방에 넣을수 있는 보석은
# 뒤에 큰 가방에도 넣을수 있다
for bag in bags:
    while jew:
        m, v = jew.pop()
        if m > bag:
            jew.append((m, v))
            break
        heappush(heap, (-v, m))

    if heap:
        v, m = heappop(heap)
        if m > bag:
            heappush(heap, (v, m))
            continue
        answer += -v
print(answer)