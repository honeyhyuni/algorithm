# https://programmers.co.kr/learn/courses/30/lessons/87946
from itertools import permutations


def solution(k, dungeons):
    answer = -1
    per = list(permutations(dungeons, len(dungeons)))

    for i in per:
        cnt, temp = 0, k
        for j in i:
            if j[0] <= temp:
                temp -= j[1]
                cnt += 1
        answer = max(answer, cnt)

    return answer


print(solution(80, [[80, 20], [50, 40], [30, 10]]))
