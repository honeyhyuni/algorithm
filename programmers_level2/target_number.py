# https://programmers.co.kr/learn/courses/30/lessons/43165
from collections import deque


def solution(numbers, target):
    answer = 0
    q = deque()
    q.append([0, numbers[0]])
    q.append([0, -numbers[0]])
    while q:
        x, ans = q.popleft()
        if x == len(numbers) - 1 and ans == target:
            answer += 1
        if x + 1 < len(numbers):
            q.append([x + 1, ans + numbers[x + 1]])
            q.append([x + 1, ans - numbers[x + 1]])
    return answer


print(solution([1, 1, 1, 1, 1], 3))
print(solution([4, 1, 2, 1], 4))
