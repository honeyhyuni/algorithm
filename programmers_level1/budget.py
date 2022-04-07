# https://programmers.co.kr/learn/courses/30/lessons/12982
def solution(d, budget):
    d.sort()
    answer, result = 0, 0
    for i in range(len(d)):
        answer += d[i]
        result += 1
        if answer > budget:
            result -= 1
            break

    return result


print(solution([1, 3, 2, 5, 4], 9))
print(solution([2, 2, 3, 3], 10))
