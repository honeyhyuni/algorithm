# https://programmers.co.kr/learn/courses/30/lessons/12922
def solution(n):
    answer = "수박"
    n, i = divmod(n, 2)
    if i == 0:
        return answer * n
    return answer * n + "수"

print(solution(3))
print(solution(4))