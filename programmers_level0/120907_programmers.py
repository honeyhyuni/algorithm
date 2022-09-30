# https://school.programmers.co.kr/learn/courses/30/lessons/120907
def solution(quiz):
    answer = []
    for i in quiz:
        i = i.split()
        if i[1] == "-":
            if int(i[0]) - int(i[2]) == int(i[4]):
                answer.append("O")
                continue
        else:
            if int(i[0]) + int(i[2]) == int(i[4]):
                answer.append("O")
                continue
        answer.append("X")
    return answer


print(solution(["3 - 4 = -3", "5 + 6 = 11"]))
print(solution(["19 - 6 = 13", "5 + 66 = 71", "5 - 15 = 63", "3 - 1 = 2"]))