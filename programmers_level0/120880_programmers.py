# https://school.programmers.co.kr/learn/courses/30/lessons/120880
def solution(numlist, n):
    answer = []
    temp = []
    for i in numlist:
        temp.append((i, abs(i - n)))
    [answer.append(i[0]) for i in sorted(temp, key=lambda x: (x[1], -x[0]))]
    return answer


print(solution([1, 2, 3, 4, 5, 6], 4))
