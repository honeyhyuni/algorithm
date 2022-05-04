# https://programmers.co.kr/learn/courses/30/lessons/12904
def solution(s):
    max_v = 1
    for i in range(len(s)):
        for j in range(i+1, len(s)+1):
            x = s[i:j]
            if x == x[::-1]:
                max_v = max(max_v, len(x))
    return max_v


print(solution("abcdcba"))
print(solution("abacde"))
print(solution("sfddfssdfsdf"))
