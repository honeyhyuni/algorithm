# https://programmers.co.kr/learn/courses/30/lessons/72413
import sys
from heapq import heappop, heappush


def solution(n, s, a, b, fares):
    arr = [[] for i in range(n + 1)]
    for i, j, k in fares:
        arr[i].append([j, k])
        arr[j].append([i, k])
    start = dijkstra(s, arr)
    min_v = start[a] + start[b]
    for i in range(1, n+1):
        dp = dijkstra(i, arr)
        min_v = min(min_v, start[i] + dp[a] + dp[b])
    return min_v


def dijkstra(start, arr):
    INF = sys.maxsize
    dp = [INF] * len(arr)
    heap = []
    dp[start] = 0
    heappush(heap, [0, start])
    while heap:
        x, y = heappop(heap)
        if dp[y] < x:
            continue
        for n_n, n_w in arr[y]:
            min_v = x + n_w
            if dp[n_n] > min_v:
                dp[n_n] = min_v
                heappush(heap, [min_v, n_n])
    return dp


print(solution(6, 4, 6, 2,
               [[4, 1, 10], [3, 5, 24], [5, 6, 2], [3, 1, 41], [5, 1, 24], [4, 6, 50], [2, 4, 66], [2, 3, 22],
                [1, 6, 25]]))
print(solution(7, 3, 4, 1, [[5, 7, 9], [4, 6, 4], [3, 6, 1], [3, 2, 3], [2, 1, 6]]))
print(solution(6, 4, 5, 6, [[2,6,6], [6,3,7], [4,6,7], [6,5,11], [2,5,12], [5,3,20], [2,4,8], [4,3,9]]))