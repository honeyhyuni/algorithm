# https://programmers.co.kr/learn/courses/30/lessons/42889
from heapq import heappop, heappush


def solution(N, stages):
    answer = []
    len_ = len(stages)
    heap = []
    for i in range(1, N + 1):
        if stages.count(i) == 0:
            heappush(heap, [0, i])
        else:
            heappush(heap, [-stages.count(i) / len_, i])
            len_ -= stages.count(i)
    while heap:
        x, y = heappop(heap)
        answer.append(y)
    return answer


print(solution(5, [2, 1, 2, 6, 2, 4, 3, 3]))
print(solution(4, [4, 4, 4, 4, 4]))
