# https://programmers.co.kr/learn/courses/30/lessons/12980
def solution(n):
    cnt = 0
    while n >= 1:
        if n % 2 == 0:
            n //= 2
        else:
            n -= 1
            cnt += 1
    return cnt


print(solution(5))
print(solution(6))
print(solution(5000))