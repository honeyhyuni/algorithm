# https://programmers.co.kr/learn/courses/30/lessons/43163
from collections import deque


def solution(begin, target, words):
    if target not in words:
        return 0
    q = deque()
    q.append([begin, 0])
    while q:
        x, cnt = q.popleft()
        if x == target:
            return cnt
        for i in range(len(words)):
            c = 0
            for _ in range(len(words[i])):
                if x[_] != words[i][_]:
                    c += 1
            if c == 1:
                q.append([words[i], cnt + 1])


print(solution("hit", "cog", ["hot", "dot", "dog", "lot", "log", "cog"]))
print(solution("hit", "cog", ["hot", "dot", "dog", "lot", "log"]))
