# https://programmers.co.kr/learn/courses/30/lessons/12906
def solution(arr):
    answer = []
    for i in arr:
        if answer and answer[-1] == i:
            continue
        answer.append(i)
    return answer

print(solution([1,1,3,3,0,1,1]))
print(solution([4,4,4,3,3]))