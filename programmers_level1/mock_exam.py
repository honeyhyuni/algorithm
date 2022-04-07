# https://programmers.co.kr/learn/courses/30/lessons/42840
def solution(answers):
    a = [1, 2, 3, 4, 5]
    a2 = [2, 1, 2, 3, 2, 4, 2, 5]
    a3 = [3, 3, 1, 1, 2, 2, 4, 4, 5, 5]
    answer = [0, 0, 0]
    result = []
    for i in range(len(answers)):
        if answers[i] == a[i % 5]:
            answer[0] += 1
        if answers[i] == a2[i % 8]:
            answer[1] += 1
        if answers[i] == a3[i % 10]:
            answer[2] += 1
    for i in range(3):
        if answer[i] == max(answer):
            result.append(i + 1)
    return result
