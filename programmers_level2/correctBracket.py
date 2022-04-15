# https://programmers.co.kr/learn/courses/30/lessons/12909
def solution(s):
    stack = []
    for i in s:
        if not stack and i == "(":
            stack.append(i)
        elif not stack and i == ")":
            return False
        elif i == ")":
            if stack[-1] == "(":
                stack.pop()
            else:
                return False
        else:
            stack.append(i)
    if stack:
        return False
    return True

print(solution("()()"))
print(solution("(())()"))
print(solution(")()("))
print(solution("(()("))