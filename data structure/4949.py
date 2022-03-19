# https://www.acmicpc.net/problem/4949
while True:
    arr = input()
    if arr == ".":
        break
    stack = []
    bol = True
    for i in arr:
        if i == "(" or i == "[":
            stack.append(i)
        elif i == ")":
            if not stack or stack[-1] == "[":
                bol = False
                break
            elif stack[-1] == "(":
                stack.pop()
        elif i == "]":
            if not stack or stack[-1] == "(":
                bol = False
                break
            elif stack[-1] == "[":
                stack.pop()
    if bol and not stack:
        print("yes")
    else:
        print("no")
