# https://school.programmers.co.kr/learn/courses/30/lessons/120956
def solution(babbling):
    answer = 0
    ori = ["aya", "ye", "woo", "ma"]
    for i in babbling:
        for j in range(4):
            i = i.replace(ori[j], str(j))
        if not i.isnumeric():
            continue
        else:
            stack = []
            for _ in i:
                if stack:
                    if stack[-1] == _:
                        break
                stack.append(_)
            else:
                answer += 1
    return answer


print(solution(["aya", "yee", "u", "maa"]))
print(solution(["ayaye", "uuu", "yeye", "yemawoo", "ayaayaa"]))