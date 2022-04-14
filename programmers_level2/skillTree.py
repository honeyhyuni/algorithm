# https://programmers.co.kr/learn/courses/30/lessons/49993
import sys


def solution(skill, skill_trees):
    answer = 0
    for i in skill_trees:
        stack = []
        for j in skill:
            temp = i.find(j)
            if temp == -1:
                stack.append(sys.maxsize)
                continue
            if stack and stack[-1] > temp:
                break
            stack.append(temp)
        else:
            answer += 1
    return answer


print(solution("CBD", ["BACDE", "CBADF", "AECB", "BDA"]))