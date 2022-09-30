# https://school.programmers.co.kr/learn/courses/30/lessons/120808
import math


def solution(denum1, num1, denum2, num2):
    answer = []
    temp = num1 * num2 // math.gcd(num1, num2)
    denum1 *= temp // num1
    denum2 *= temp // num2
    t = math.gcd(denum1 + denum2, temp)

    answer.append((denum1 + denum2) // t)
    answer.append(temp // t)

    return answer


print(solution(1, 2, 3, 4))
print(solution(9, 2, 1, 3))
