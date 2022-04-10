# https://programmers.co.kr/learn/courses/30/lessons/12934
import math


def solution(n):
    if int(math.sqrt(n)) ** 2 == n:
        return (int(math.sqrt(n)) + 1) ** 2
    else:
        return -1


print(solution(121))
print(solution(3))
