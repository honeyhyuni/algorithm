# https://school.programmers.co.kr/learn/courses/30/lessons/142085
from heapq import heappop, heappush, heapify


def solution(n, k, enemy):
    heap = enemy[:k]
    heapify(heap)
    for i in range(k, len(enemy)):
        heappush(heap, enemy[i])
        n -= heappop(heap)
        if n < 0:
            return i
    return len(enemy)


print(solution(7, 3, [4, 2, 4, 5, 3, 3, 1]))
print(solution(2, 4, [3, 3, 3, 3]))
