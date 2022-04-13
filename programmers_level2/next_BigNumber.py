# https://programmers.co.kr/learn/courses/30/lessons/12911
def solution(n):
    one_c = bin(n).count("1")
    for i in range(n+1, 1000000):
        if one_c == bin(i).count("1"):
            return i



print(solution(78))
print(solution(15))