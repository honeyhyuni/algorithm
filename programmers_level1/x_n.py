# https://programmers.co.kr/learn/courses/30/lessons/12954
def solution(x, n):
    return [i * x + x for i in range(n)]

print(solution(2, 5))
print(solution(4, 3))
print(solution(-4, 2))