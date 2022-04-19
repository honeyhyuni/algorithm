# https://www.acmicpc.net/problem/23350
import sys
input = sys.stdin.readline
from collections import deque
from heapq import heappop, heappush
q = deque()
result = 0
n, m = map(int, input().split())

for i in range(n):
    a, b = map(int, input().split())
    q.append([a, b])
while q:
    len_q = len(q)
    heap = []
    for i in range(len_q):
        p, w = q.popleft()
        result += w
        if p != m:
            if not heap:
                q.append([p, w])
            else:
                bol = True
                for _ in range(len(q)):
                    if q[_][0] == m:
                        bol = False
                if bol:
                    q.appendleft([p, w])
                    result -= w
                    break
                else:
                    q.append([p, w])
        else:
            heappush(heap, w)
            if heap[0] < w:
                juckjae = []
                while heap[0] != w:
                    x = heappop(heap)
                    juckjae.append(x)
                    result += x
                result += sum(juckjae)
                while juckjae:
                    heappush(heap, juckjae.pop())
    m -= 1
print(result)
