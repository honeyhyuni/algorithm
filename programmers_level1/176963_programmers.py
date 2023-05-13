# https://school.programmers.co.kr/learn/courses/30/lessons/176963
def solution(name, yearning, photo):
    answer = []
    for i in photo:
        grade = 0
        for j in i:
            try:
                t = name.index(j)
                grade += yearning[t]
            except:
                continue
        answer.append(grade)
    return answer


print(solution(["may", "kein", "kain", "radi"], [5, 10, 1, 3],
               [["may", "kein", "kain", "radi"], ["may", "kein", "brin", "deny"], ["kon", "kain", "may", "coni"]]))
