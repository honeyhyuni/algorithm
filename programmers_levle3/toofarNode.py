# https://programmers.co.kr/learn/courses/30/lessons/49189
import sys
from heapq import heappop, heappush


def solution(n, edge):
    answer = 0
    INF = sys.maxsize
    arr = [[] for i in range(n + 1)]
    for i in edge:
        arr[i[0]].append([i[1], 1])
        arr[i[1]].append([i[0], 1])
    dp = [INF] * (n + 1)
    dp[1] = 0
    heap = []
    heappush(heap, [0, 1])

    while heap:
        x, y = heappop(heap)
        if dp[y] < x:
            continue
        for n_n, n_w in arr[y]:
            min_v = x + n_w
            if dp[n_n] > min_v:
                dp[n_n] = min_v
                heappush(heap, [min_v, n_n])
    for i in dp[2:]:
        if i == max(dp[2:]):
            answer += 1
    return answer


print(solution(6, [[3, 6], [4, 3], [3, 2], [1, 3], [1, 2], [2, 4], [5, 2]]))
