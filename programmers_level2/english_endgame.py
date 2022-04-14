# https://programmers.co.kr/learn/courses/30/lessons/12981
from builtins import enumerate


def solution(n, words):
    stack = []
    for i, j in enumerate(words):
        if stack and stack[-1][-1] != j[0] or j in stack:
            v, mod = divmod(i + 1, n)
            if mod > 0:
                return [mod, v + 1]
            else:
                return [n, v]
        stack.append(j)

    return [0, 0]


print(solution(3, ["tank", "kick", "know", "wheel", "land", "dream", "mother", "robot", "tank"]))
print(solution(5,
               ["hello", "observe", "effect", "take", "either", "recognize", "encourage", "ensure", "establish", "hang",
                "gather", "refer", "reference", "estimate", "executive"]))
print(solution(2, ["hello", "one", "even", "never", "now", "world", "draw"]))
