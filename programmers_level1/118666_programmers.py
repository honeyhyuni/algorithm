# https://school.programmers.co.kr/learn/courses/30/lessons/118666
def solution(survey, choices):
    ts = {"R": 0, "T": 0, "C": 0, "F": 0, "J": 0, "M": 0, "A": 0, "N": 0}
    for i, j in zip(survey, choices):
        if j < 4:
            ts[i[0]] += 4 - j
        else:
            ts[i[1]] += j - 4
    answer = ''
    for i, j in [("R", "T"), ("C", "F"), ("J", "M"), ("A", "N")]:
        if ts[i] >= ts[j]:
            answer += i
        else:
            answer += j
    return answer


print(solution(["AN", "CF", "MJ", "RT", "NA"], [5, 3, 2, 7, 5]))
print(solution(["TR", "RT", "TR"], [7, 1, 3]))