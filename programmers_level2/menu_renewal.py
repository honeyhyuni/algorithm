# https://programmers.co.kr/learn/courses/30/lessons/72411
from collections import Counter
from itertools import combinations


def solution(orders, course):
    answer = []
    for _ in course:
        temp = []
        for i in orders:
            comb = list(combinations(sorted(i), _))
            temp += comb
        c = Counter(temp)
        if len(c) != 0 and max(c.values()) > 1:
            for i in c:
                if c[i] == max(c.values()):
                    answer.append("".join(i))
    answer.sort()
    return answer


print(solution(["ABCFG", "AC", "CDE", "ACDE", "BCFG", "ACDEH"], [2, 3, 4]))
print(solution(["ABCDE", "AB", "CD", "ADE", "XYZ", "XYZ", "ACD"], [2,3,5]))
print(solution(["XYZ", "XWY", "WXA"], [2,3,4]))