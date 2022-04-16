# https://programmers.co.kr/learn/courses/30/lessons/64065
def solution(s):
    answer = []
    s = s[2:-2]
    s = s.split("},{")
    s.sort(key= lambda x: len(x))
    for i in s:
        i = i.split(",")
        for j in i:
            if int(j) not in answer:
                answer.append(int(j))
    return answer


print(solution("{{2},{2,1},{2,1,3},{2,1,3,4}}"))
print(solution("{{1,2,3},{2,1},{1,2,4,3},{2}}"))
print(solution("{{20,111},{111}}"))
print(solution("{{123}}"))
print(solution("{{4,2,3},{3},{2,3,4,1},{2,3}}"))