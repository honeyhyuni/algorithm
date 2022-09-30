# https://school.programmers.co.kr/learn/courses/30/lessons/120896
def solution(s):
    answer = ''
    alp = [0] * 26
    for i in s:
        alp[ord(i) - 97] += 1
    for i in range(26):
        if alp[i] == 1:
            answer += chr(i + 97)
    return answer


print(solution("abcabcadc"))
