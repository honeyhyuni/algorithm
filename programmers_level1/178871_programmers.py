# https://school.programmers.co.kr/learn/courses/30/lessons/178871
from collections import defaultdict


def solution(players, callings):
    dic = defaultdict(int)
    for i in range(len(players)):
        dic[players[i]] = i
    for i in range(len(callings)):
        v = dic[callings[i]]
        dic[callings[i]] -= 1
        dic[players[v-1]] += 1
        players[v], players[v-1] = players[v-1], players[v]

    return players


print(solution(["mumu", "soe", "poe", "kai", "mine"], ["kai", "kai", "mine", "mine"]))

