# https://school.programmers.co.kr/learn/courses/30/lessons/154539
def solution(numbers):
    n = len(numbers)
    answer = [-1] * n
    stack = []
    for i in range(n):
        while stack and numbers[stack[-1]] < numbers[i]:
            temp = stack.pop()
            answer[temp] = numbers[i]
        stack.append(i)
    return answer


print(solution([2, 3, 3, 5]))
print(solution([9, 1, 5, 3, 6, 2]))