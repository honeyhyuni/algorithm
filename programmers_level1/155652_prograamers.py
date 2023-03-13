# https://school.programmers.co.kr/learn/courses/30/lessons/155652
def solution(s, skip, index):
    answer = ''
    skip_set = set([ord(i) for i in skip])
    for i in s:
        cnt = 0
        temp = ord(i)
        while cnt < index:
            temp += 1
            if temp > 122:
                temp = 97
            if temp not in skip_set:
                cnt += 1
        answer += chr(temp)
    return answer


print(solution("aukks", "wbqd", 5))
print(solution("abc", "abc", 3))
