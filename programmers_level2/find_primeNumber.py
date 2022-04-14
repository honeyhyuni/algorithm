# https://programmers.co.kr/learn/courses/30/lessons/42839
from itertools import permutations as p


def solution(numbers):
    answer = 0
    temp = []
    for i in range(1, len(numbers)+1):
        perm = list(p(numbers, i))
        for per in perm:
            t = int("".join(per))
            if t in temp or (t == 0 or t == 1):
                continue
            temp.append(int("".join(per)))
            for j in range(2, t):
                if t % j == 0:
                    break
            else:
                answer += 1
    return answer


print(solution("17"))
print(solution("011"))
