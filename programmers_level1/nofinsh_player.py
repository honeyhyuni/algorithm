# https://programmers.co.kr/learn/courses/30/lessons/42576
def solution(participant, completion):
    dic = {}
    for i in participant:
        if i in dic:
            dic[i] += 1
        else:
            dic[i] = 1
    for i in completion:
        dic[i] -= 1
    for i, j in dic.items():
        if j == 1:
            answer = i
            break
    return answer


print(solution(["marina", "josipa", "nikola", "vinko", "filipa"], ["josipa", "filipa", "marina", "nikola"]))