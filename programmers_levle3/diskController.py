# https://programmers.co.kr/learn/courses/30/lessons/42627
from heapq import heappop, heappush


def solution(jobs):
    answer = 0
    start, end, idx = -1, 0, 0
    heap = []
    while idx < len(jobs):
        for j in jobs:
            if start < j[0] <= end:
                heappush(heap, [j[1], j[0]])
        if heap:
            es, ss = heappop(heap)
            start = end
            end += es
            answer += end - ss
            idx += 1
        else:
            end += 1
    return answer // len(jobs)


print(solution([[0, 3], [1, 9], [2, 6]]))
