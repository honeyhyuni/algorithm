def solution(food):
    answer = ''
    for i in range(1, len(food)):
        answer += str(i) * (food[i] // 2)
    answer += '0'
    return answer + answer[:-1][::-1]


print(solution([1, 3, 4, 6]))
print(solution([1, 7, 1, 2]))
