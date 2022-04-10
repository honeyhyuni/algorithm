# https://programmers.co.kr/learn/courses/30/lessons/12950
def solution(arr1, arr2):
    answer = []
    for i, j in zip(arr1, arr2):
        temp = []
        for a, b in zip(i, j):
            temp.append(a+b)
        answer.append(temp)
    return answer


print(solution([[1,2],[2,3]], [[3,4],[5,6]]))
print(solution([[1],[2]], [[3],[4]]))