# https://programmers.co.kr/learn/courses/30/lessons/42842
def solution(brown, yellow):
    temp = brown + yellow
    for i in range(1, temp+1):
        if temp % i == 0:
            a = temp // i
            if a >= i:
                if 2 * a + 2 * i == brown + 4:
                    return [a, i]

print(solution(10, 2))
print(solution(8, 1))
print(solution(24, 24))