# https://programmers.co.kr/learn/courses/30/lessons/43164
from collections import defaultdict


def solution(tickets):
    answer = []
    dic = defaultdict(list)
    for i in tickets:
        dic[i[0]].append(i[1])

    for i in dic.keys():
        dic[i].sort(reverse=True)
    stack = ["ICN"]
    while stack:
        v = stack[-1]
        if not dic[v]:
            answer.append(stack.pop())
        else:
            stack.append(dic[v].pop())
    return answer[::-1]

print(solution([["ICN", "JFK"], ["HND", "IAD"], ["JFK", "HND"]]))
print(solution([["ICN", "SFO"], ["ICN", "ATL"], ["SFO", "ATL"], ["ATL", "ICN"], ["ATL", "SFO"]]))
