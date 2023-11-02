# https://school.programmers.co.kr/learn/courses/30/lessons/136798


def solution(number, limit, power):
    answer = 0
    for num in range(1, number+1):
        temp = 0
        for n in range(1, int(num**(1/2))+1):
            if num % n == 0:
                if n ** 2 != num:
                    temp += 2
                else:
                    temp += 1
                if temp > limit:
                    answer += power
                    break
        else:
            answer += temp
    return answer


print(solution(5, 3, 2))
print(solution(10, 3, 2))