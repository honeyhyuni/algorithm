# https://programmers.co.kr/learn/courses/30/lessons/12939
def solution(s):
    s = list(map(int, s.split()))
    return str(min(s)) + " " + str(max(s))


print(solution("1 2 3 4"))
print(solution("-1 -2 -3 -4"))
print(solution("-1 -1"))