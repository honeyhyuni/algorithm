# https://programmers.co.kr/learn/courses/30/lessons/42890
from itertools import combinations


def solution(relation):
    answer = []
    n = len(relation[0])
    lst = [i for i in range(n)]
    for i in range(1, n + 1):
        combo = list(combinations(lst, i))
        for c in combo:
            a = []
            for j in relation:
                temp = []
                for cc in c:
                    temp.append(j[cc])
                if temp in a:
                    break
                a.append(temp)
            else:
                for _ in answer:
                    if set(_).issubset(c):
                        break
                else:
                    answer.append(c)

    return len(answer)


print(solution([["100", "ryan", "music", "2"], ["200", "apeach", "math", "2"], ["300", "tube", "computer", "3"],
                ["400", "con", "computer", "4"], ["500", "muzi", "music", "3"], ["600", "apeach", "music", "2"]]))
