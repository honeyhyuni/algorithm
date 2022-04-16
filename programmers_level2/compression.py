# https://programmers.co.kr/learn/courses/30/lessons/17684
def solution(msg):
    answer = []
    dic = {}
    for i in range(26):
        dic[chr(65 + i)] = i + 1
    cnt = 27
    idx = 0
    temp = ""
    while idx < len(msg):
        temp += msg[idx]
        if temp not in dic:
            dic[temp] = cnt
            cnt += 1
            answer.append(dic[temp[:-1]])
            temp = ""
        else:
            idx += 1
    answer.append(dic[temp])
    return answer

print(solution("KAKAO"))
print(solution("TOBEORNOTTOBEORTOBEORNOT"))
print(solution("ABABABABABABABAB"))