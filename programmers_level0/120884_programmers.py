# https://school.programmers.co.kr/learn/courses/30/lessons/120884
def solution(chicken):
    answer = 0
    while chicken >= 10:
        chicken, mod = divmod(chicken, 10)
        answer += chicken
        chicken += mod
    return answer


print(solution(100))
print(solution(1081))