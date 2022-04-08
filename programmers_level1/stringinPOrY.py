# https://programmers.co.kr/learn/courses/30/lessons/12916
def solution(s):
    a, b = 0, 0
    a += s.count("p") + s.count("P")
    b += s.count("y") + s.count("Y")
    return a == b


print(solution("pPoooyY"))