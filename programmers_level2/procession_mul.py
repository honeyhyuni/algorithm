# https://programmers.co.kr/learn/courses/30/lessons/12949
def solution(arr1, arr2):
    answer = []
    arr2 = list(zip(*arr2))
    for i in arr1:
        temp = []
        for j in arr2:
            re = 0
            for _ in range(len(j)):
                re += i[_] * j[_]
            temp.append(re)
        answer.append(temp)
    return answer


print(solution([[1, 4], [3, 2], [4, 1]], [[3, 3], [3, 3]]))
print(solution([[2, 3, 2], [4, 2, 4], [3, 1, 4]], [[5, 4, 3], [2, 4, 1], [3, 1, 1]]))