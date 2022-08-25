# https://school.programmers.co.kr/learn/courses/30/lessons/118669
from heapq import heappop, heappush
import sys


def solution(n, paths, gates, summits):
    arr = [[] for i in range(n + 1)]
    for i, j, k in paths:
        arr[i].append((j, k))
        arr[j].append((i, k))
    INF = sys.maxsize
    dp = [INF] * (n+1)
    summits = set(summits)

    result = []

    heap = []
    for i in gates:
        heappush(heap, (0, i))
    while heap:
        c, x = heappop(heap)
        if x in summits or c > dp[x]:
            continue
        for n_n, n_w in arr[x]:
            max_v = max(n_w, c)
            if max_v < dp[n_n]:
                dp[n_n] = max_v
                heappush(heap, (max_v, n_n))
    for i in summits:
        result.append([i, dp[i]])
    result.sort(key= lambda x: (x[1], x[0]))
    return result[0]


print(solution(6, [[1, 2, 3], [2, 3, 5], [2, 4, 2], [2, 5, 4], [3, 4, 4], [4, 5, 3], [4, 6, 1], [5, 6, 1]],
               [1, 3], [5]))
print(solution(7, [[1, 4, 4], [1, 6, 1], [1, 7, 3], [2, 5, 2], [3, 7, 4], [5, 6, 6]],
               [1], [2, 3, 4]))
print(solution(7, [[1, 2, 5], [1, 4, 1], [2, 3, 1], [2, 6, 7], [4, 5, 1], [5, 6, 1], [6, 7, 1]],
               [3, 7], [1, 5]))
print(solution(5, [[1, 3, 10], [1, 4, 20], [2, 3, 4], [2, 4, 6], [3, 5, 20], [4, 5, 6]],
               [1, 2], [5]))
