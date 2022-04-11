# https://programmers.co.kr/learn/courses/30/lessons/12978
# 다익스트라
import sys
from heapq import heappop, heappush


def solution(N, road, K): 
    answer = 0
    INF = sys.maxsize
    dp = [INF] * (N + 1)
    arr = [[] for i in range(N + 1)]
    heap = []
    for i in road:
        arr[i[0]].append([i[1], i[2]])
        arr[i[1]].append([i[0], i[2]])
    heappush(heap, [0, 1])
    dp[1] = 0
    while heap:
        x, y = heappop(heap)
        if dp[y] < x:
            continue
        for n_n, n_w in arr[y]:
            min_v = x + n_w
            if dp[n_n] > min_v:
                dp[n_n] = min_v
                heappush(heap, [min_v, n_n])
    for i in dp[1:]:
        if i <= K:
            answer += 1

    return answer


print(solution(5, [[1, 2, 1], [2, 3, 3], [5, 2, 2], [1, 4, 2], [5, 3, 1], [5, 4, 2]], 3))
print(solution(6, [[1, 2, 1], [1, 3, 2], [2, 3, 2], [3, 4, 3], [3, 5, 2], [3, 5, 3], [5, 6, 1]], 4))
