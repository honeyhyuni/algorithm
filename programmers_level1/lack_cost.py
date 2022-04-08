# https://programmers.co.kr/learn/courses/30/lessons/82612
def solution(price, money, count):
    answer = 0
    for i in range(1, count+1):
        answer += price * i
    if answer - money > 0:
        return answer - money
    else:
        return 0


print(solution(3, 20, 4))
