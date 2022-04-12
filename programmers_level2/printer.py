# https://programmers.co.kr/learn/courses/30/lessons/42587
from collections import deque


def solution(priorities, location):
    answer = 0
    prior = deque(priorities)
    arr = deque(i for i in range(len(prior)))
    while prior:
        max_v = max(prior)
        x = prior.popleft()
        y = arr.popleft()
        if x != max_v:
            prior.append(x)
            arr.append(y)
            continue
        else:
            if y == location:
                return answer + 1
            else:
                answer += 1
    return answer


print(solution([2, 1, 3, 2], 2))
print(solution([1, 1, 9, 1, 1, 1], 0))
