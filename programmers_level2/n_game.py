# https://programmers.co.kr/learn/courses/30/lessons/17687
from collections import deque


def solution(n, t, m, p):
    dic = {10: "A", 11: "B", 12: "C", 13: "D", 14: "E", 15: "F"}
    answer = [0, 1]
    result = ""
    for i in range(2, m*t):
        q = deque()
        while True:
            i, mod = divmod(i, n)
            q.appendleft(mod)
            if i == 0:
                while q:
                    answer.append(q.popleft())
                break
    for i in range(0, len(answer), m):
        if len(answer[i:i + m]) < p:
            continue
        if answer[i:i + m][p - 1] >= 10:
            result += dic[answer[i:i + m][p - 1]]
        else:
            result += str(answer[i:i + m][p - 1])
        if len(result) == t:
            break
    return result


print(solution(2, 4, 2, 1))
print(solution(16, 16, 2, 1))
print(solution(16, 16, 2, 2))
