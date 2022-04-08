# https://programmers.co.kr/learn/courses/30/lessons/12903
def solution(s):
    n = len(s)
    if n % 2 == 0:
        answer = s[n//2-1:n//2+1]
    else:
        answer = s[n//2]

    return answer


print(solution("abcde"))
print(solution("qwer"))