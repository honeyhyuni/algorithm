# https://programmers.co.kr/learn/courses/30/lessons/42626
from heapq import heappop, heappush, heapify


def solution(scoville, K):
    answer = 0
    heapify(scoville)
    while scoville[0] < K and len(scoville) > 1:
        x = heappop(scoville)
        y = heappop(scoville)
        heappush(scoville, x + y * 2)
        answer += 1
    if scoville[0] >= K:
        return answer
    else:
        return -1


print(solution([1, 2, 3, 9, 10, 12], 7))
