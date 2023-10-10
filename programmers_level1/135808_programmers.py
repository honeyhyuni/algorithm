# https://school.programmers.co.kr/learn/courses/30/lessons/135808


def solution(k, m, score):
    answer = 0
    score.sort(reverse=True)
    for i in range(0, len(score), m):
        if i + m <= len(score):
            answer += min(score[i:i+m]) * m
    return answer


print(solution(3, 4, [1, 2, 3, 1, 2, 3, 1]))
print(solution(4, 3, [4, 1, 2, 2, 4, 4, 4, 4, 1, 2, 4, 2]))
