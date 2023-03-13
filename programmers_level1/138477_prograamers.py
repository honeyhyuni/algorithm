# https://school.programmers.co.kr/learn/courses/30/lessons/138477
from heapq import heappop, heappush


def solution(k, score):
    answer = []
    heap = []
    for i in score:
        heappush(heap, i)
        if len(heap) > k:
            heappop(heap)
        answer.append(heap[0])
    return answer


print(solution(3, [10, 100, 20, 150, 1, 100, 200]))
