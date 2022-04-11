# https://programmers.co.kr/learn/courses/30/lessons/42586/solution_groups?language=python3
from collections import deque


def solution(progresses, speeds):
    answer = []
    stack = []
    q = deque()
    for i, j in zip(progresses, speeds):
        temp, c = divmod((100 - i), j)
        if c > 0:
            temp += 1
        q.append(temp)
    cnt = 1
    stack.append(q.popleft())
    while q:
        x = q.popleft()
        if stack[-1] >= x:
            cnt += 1
        else:
            stack.append(x)
            answer.append(cnt)
            cnt = 1
    answer.append(cnt)
    return answer


print(solution([93, 30, 55], [1, 30, 5]))