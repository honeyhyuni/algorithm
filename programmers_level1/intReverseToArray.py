# https://programmers.co.kr/learn/courses/30/lessons/12932
def solution(n):
    answer = []
    n = str(n)
    for i in range(len(n)-1, -1, -1):
        answer.append(int(n[i]))
    return answer

print(solution(12345))