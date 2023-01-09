# https://school.programmers.co.kr/learn/courses/30/lessons/138476
from collections import Counter


def solution(k, tangerine):
    answer = 0
    for i, j in Counter(tangerine).most_common():
        k -= j
        answer += 1
        if k <= 0:
            break
    return answer


print(solution(6, [1, 3, 2, 5, 4, 5, 2, 3]))
