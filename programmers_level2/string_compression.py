# https://programmers.co.kr/learn/courses/30/lessons/60057
def solution(s):
    answer = len(s)
    for i in range(1, len(s)//2+1):
        temp = s[:i]
        cnt = 1
        tt = ""
        for j in range(i, len(s), i):
            if temp == s[j:j+i]:
                cnt += 1
            else:
                if cnt > 1:
                    tt += str(cnt) + temp
                else:
                    tt += temp
                temp = s[j:j + i]
                cnt = 1
        if cnt > 1:
            tt += str(cnt) + temp
        else:
            tt += temp
        answer = min(answer, len(tt))
    return answer

print(solution("aabbaccc"))
print(solution("ababcdcdababcdcd"))
print(solution("abcabcdede"))
print(solution("abcabcabcabcdededededede"))
print(solution("xababcdcdababcdcd"))