# https://school.programmers.co.kr/learn/courses/30/lessons/147355?language=python3
def solution(t, p):
    answer = 0
    for i in range(len(t) - len(p) + 1):
        if int(t[i:i + len(p)]) <= int(p):
            answer += 1
    return answer


print(solution("3141592", "271"))
