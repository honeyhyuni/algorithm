# https://school.programmers.co.kr/learn/courses/30/lessons/135807
import math


def solution(arrayA, arrayB):
    agc, bgc = 0, 0
    for i in arrayA:
        agc = math.gcd(agc, i)
    for i in arrayB:
        bgc = math.gcd(bgc, i)

    for i, j in zip(arrayA, arrayB):
        if i % bgc == 0:
            bgc = 1
        if j % agc == 0:
            agc = 1
    if agc == 1 and bgc == 1:
        return 0
    return max(agc, bgc)


print(solution([10, 17], [5, 20]))
print(solution([10, 20], [5, 17]))
print(solution([14, 35, 119], [18, 30, 102]))
