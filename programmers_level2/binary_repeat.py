# https://programmers.co.kr/learn/courses/30/lessons/70129
def solution(s):
    cnt = 0
    answer = 0
    while int(s) > 1:
        temp = s.count("1")
        answer += s.count("0")
        s = bin(temp)[2:]
        cnt += 1
    return [cnt, answer]


print(solution("110010101001"))
print(solution("01110"))
print(solution("1111111"))