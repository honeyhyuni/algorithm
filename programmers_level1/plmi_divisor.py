# https://programmers.co.kr/learn/courses/30/lessons/77884
def solution(left, right):
    answer = []
    for i in range(left, right + 1):
        temp = 0
        for j in range(1, i + 1):
            if i % j == 0:
                temp += 1
        if temp % 2 == 0:
            answer.append(i)
        else:
            answer.append(-i)
    return sum(answer)


print(solution(13, 17))
print(solution(24, 27))
