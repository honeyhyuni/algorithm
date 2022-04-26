# https://programmers.co.kr/learn/courses/30/lessons/12927
from heapq import heappop, heappush
def solution(n, works):
    heap = []
    answer = 0
    if sum(works) <= n:
        return 0
    for i in works:
        heappush(heap, [-i, i])
    while n != 0:
        x, y = heappop(heap)
        x += 1
        y -= 1
        if y > 0:
            heappush(heap, [x, y])
        n -= 1
    for i, j in heap:
        answer += j * j
    return answer


print(solution(4, [4, 3, 3]))
print(solution(1, [2, 1, 2]))
print(solution(3, [1, 1]))