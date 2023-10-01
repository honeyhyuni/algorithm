# https://school.programmers.co.kr/learn/courses/30/lessons/131701
def solution(elements):
    len_ = len(elements)
    answer = set()
    for i in range(len_):
        temp = elements[i]
        answer.add(temp)
        for j in range(i+1, i+len_):
            temp += elements[j%len_]
            answer.add(temp)
    return len(answer)


print(solution([7, 9, 1, 1, 4]))
