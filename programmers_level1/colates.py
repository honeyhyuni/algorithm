# https://programmers.co.kr/learn/courses/30/lessons/12943
def solution(num):
    for i in range(500):
        if num == 1:
            return i
        if num % 2 == 0:
            num //= 2
        else:
            num = num * 3 + 1
    return -1

print(solution(6))
print(solution(16))
print(solution(626331))