# https://programmers.co.kr/learn/courses/30/lessons/64064
from itertools import permutations


def solution(user_id, banned_id):
    answer = []
    lst = list(permutations(user_id, len(banned_id)))

    for i in lst:
        if compare(i, banned_id):
            i = sorted(i)
            if i not in answer:
                answer.append(i)
    return len(answer)


def compare(v, ban):
    for i in range(len(v)):
        if len(v[i]) != len(ban[i]):
            return False
        for j in range(len(v[i])):
            if ban[i][j] == "*":
                continue
            if ban[i][j] != v[i][j]:
                return False
    return True


print(solution(["frodo", "fradi", "crodo", "abc123", "frodoc"], ["fr*d*", "abc1**"]))
print(solution(["frodo", "fradi", "crodo", "abc123", "frodoc"], ["*rodo", "*rodo", "******"]))
print(solution(["frodo", "fradi", "crodo", "abc123", "frodoc"], ["fr*d*", "*rodo", "******", "******"]))
