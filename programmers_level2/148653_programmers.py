# https://school.programmers.co.kr/learn/courses/30/lessons/148653
import copy
import sys
from collections import deque


def solution(storey):
    storey = list(map(int, str(storey)))
    q = deque()
    q.append((storey, 0))
    ans = sys.maxsize

    while q:
        x, cnt = q.popleft()
        t = x.pop()

        for i, j in enumerate([10 - t, t]):
            if len(x) > 0:
                temp = copy.deepcopy(x)
                if i == 0:
                    temp[-1] += 1
                q.append((temp, cnt + j))
            else:
                if i == 0:
                    ans = min(ans, cnt+1 + j)
                else:
                    ans = min(ans, cnt + j)
    return ans


# print(solution(909))
print(solution(16))
print(solution(2554))
# print(solution(56789742))
