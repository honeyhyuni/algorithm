# https://programmers.co.kr/learn/courses/30/lessons/17682
def solution(dartResult):
    answer = []
    dic = {"S": 1, "D": 2, "T": 3}
    temp = ""
    for i in dartResult:
        if i in dic:
            answer.append(pow(int(temp), dic[i]))
            temp = ""
        elif i == "*":
            if len(answer) > 1:
                answer[-2] *= 2
            answer[-1] *= 2
        elif i == "#":
            answer[-1] *= -1
        else:
            temp += i
    return sum(answer)


print(solution("1S2D*3T"))
print(solution("1D2S#10S"))
print(solution("1D2S0T"))
print(solution("1S*2T*3S"))
print(solution("1D#2S*3S"))
print(solution("1T2D3D#"))
print(solution("1D2S3T*"))