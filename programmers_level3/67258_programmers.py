# https://school.programmers.co.kr/learn/courses/30/lessons/67258
from collections import defaultdict


def solution(gems):
    answer = []
    s = set()
    dic = defaultdict(str)
    for i in gems:
        s.add(i)
        dic[i] = 0
    left, right = 0, 0
    n = len(gems)
    temp = set()
    while left < n and right < n:
        if len(temp) < len(s):
            dic[gems[right]] += 1
            temp.add(gems[right])
            right += 1
        else:
            dic[gems[left]] -= 1
            if dic[gems[left]] == 0:
                answer.append([left + 1, right, right - left])
                temp.remove(gems[left])
            left += 1
    if len(temp) == len(s):
        while left < n:
            dic[gems[left]] -= 1
            if dic[gems[left]] == 0:
                answer.append([left + 1, right, right - left])
                temp.remove(gems[left])
                break
            left += 1
    answer.sort(key=lambda x: (x[2], x[0]))
    return answer[0][:2] if answer else [1, n]


print(solution(["DIA", "RUBY", "RUBY", "DIA", "DIA", "EMERALD", "SAPPHIRE", "DIA"]))
print(solution(["AA", "AB", "AC", "AA", "AC"]))
print(solution(["XYZ", "XYZ", "XYZ"]))
print(solution(["ZZZ", "YYY", "NNNN", "YYY", "BBB"]))
print(solution(["A", "B", "C", "B", "F", "D", "A", "F", "B", "D", "B"]))
print(solution(["A","A","A","B","B"]))
print(solution(["A"]))
print(solution(["A", "B", "B", "B", "B", "B", "B", "C", "B", "A"]))