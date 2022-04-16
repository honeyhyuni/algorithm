# https://programmers.co.kr/learn/courses/30/lessons/17680
from collections import deque


def solution(cacheSize, cities):
    if cacheSize == 0:
        return len(cities) * 5
    answer = 0
    q = deque()
    while cities:
        x = cities.pop(0).upper()
        if x in q:
            answer += 1
            q.remove(x)
            q.append(x)
        else:
            answer += 5
            if len(q) >= cacheSize:
                q.popleft()
            q.append(x)
    return answer


print(solution(3, ["Jeju", "Pangyo", "Seoul", "NewYork", "LA", "Jeju", "Pangyo", "Seoul", "NewYork", "LA"]))
print(solution(5,
               ["Jeju", "Pangyo", "Seoul", "NewYork", "LA", "SanFrancisco", "Seoul", "Rome", "Paris", "Jeju", "NewYork",
                "Rome"]))
