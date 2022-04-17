# https://programmers.co.kr/learn/courses/30/lessons/67257
import copy
from itertools import permutations
def solution(expression):
    op = list(permutations(["*", "-", "+"], 3))
    temp = ""
    arr = []
    for i in expression:
        if i.isdigit():
            temp += i
        else:
            arr.append(temp)
            arr.append(i)
            temp = ""
    arr.append(temp)

    max_v = 0
    for i in op:
        max_v = max(check(arr, i), max_v)
    return max_v

def check(arr, op):
    arr_ = copy.deepcopy(arr)
    for i in op:
        stack = []
        while arr_:
            x = arr_.pop(0)
            if x == i:
                if x == "*":
                    stack.append(int(stack.pop()) * int(arr_.pop(0)))
                elif x == "+":
                    stack.append(int(stack.pop()) + int(arr_.pop(0)))
                else:
                    stack.append(int(stack.pop()) - int(arr_.pop(0)))
            else:
                stack.append(x)
        arr_ = stack
    return abs(int(arr_[0]))

print(solution("100-200*300-500+20"))
print(solution("50*6-3*2"))