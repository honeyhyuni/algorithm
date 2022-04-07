# https://programmers.co.kr/learn/courses/30/lessons/68935
def solution(n):
    answer = ""
    result = 0
    while n >= 3:
        n, i = divmod(n, 3)
        answer += str(i)
    answer += str(n)
    cnt = 0
    for i in range(len(answer)-1, -1, -1):      # == result = int(answer, 3)
        result += int(answer[i]) * (3 ** cnt)
        cnt += 1

    return result


print(solution(45))
print(solution(125))