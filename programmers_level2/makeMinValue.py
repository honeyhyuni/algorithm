# https://programmers.co.kr/learn/courses/30/lessons/12941
def solution(A,B):
    answer = 0
    A.sort()
    B.sort(reverse=True)
    for i, j in zip(A, B):
        answer += i * j
    return answer

print(solution([1, 4, 2], [5, 4, 4]))
print(solution([1, 2], [3, 4]))