# https://school.programmers.co.kr/learn/courses/30/lessons/132267
def solution(a, b, n):
    answer = 0
    while n >= a:
        answer += (n // a) * b
        n = (n % a) + (n // a) * b
    return answer


print(solution(2, 1, 20))
print(solution(3, 1, 20))
print(solution(4, 3, 20))
