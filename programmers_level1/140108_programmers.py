# https://school.programmers.co.kr/learn/courses/30/lessons/140108

def solution(s):
    answer = 0
    x, x_cnt, temp_cnt = "", 0, 0
    for i in s:
        if not x:
            x = i
            x_cnt += 1
        elif x != i:
            temp_cnt += 1
        else:
            x_cnt += 1
        if x_cnt == temp_cnt:
            answer += 1
            x, x_cnt, temp_cnt = "", 0, 0
    return answer + 1 if x else answer


print(solution("banana"))
print(solution("abracadabra"))
print(solution("aaabbaccccabba"))
