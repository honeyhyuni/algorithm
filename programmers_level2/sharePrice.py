# https://programmers.co.kr/learn/courses/30/lessons/42584
from collections import deque


def solution(prices):
    q = deque(prices)
    answer = []
    while q:
        cnt = 0
        x = q.popleft()
        for i in q:
            cnt += 1
            if x > i:
                break
        answer.append(cnt)
    return answer


print(solution([1, 2, 3, 2, 3]))
