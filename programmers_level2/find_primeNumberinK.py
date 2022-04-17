# https://programmers.co.kr/learn/courses/30/lessons/92335
def solution(n, k):
    answer = 0
    k_jin, temp = '', ''
    while n > 0:
        n, mod = divmod(n, k)
        k_jin += str(mod)

    k_jin = k_jin[::-1]
    temp = k_jin.split('0')
    result = []
    for i in temp:
        if i != "1" and i != '':
            result.append(int(i))

    for i in result:
        for j in range(2, int(i**0.5)+1):
            if i % j == 0:
                break
        else:
            answer += 1
    return answer


print(solution(437674, 3))
print(solution(110011, 10))