# https://programmers.co.kr/learn/courses/30/lessons/12973
def solution(s):
    stack = []
    for i in list(s):
        if stack and stack[-1] == i:
            stack.pop()
        else:
            stack.append(i)
    if not stack:
        return 1
    else:
        return 0


print(solution("baabaa"))
print(solution("cdcd"))