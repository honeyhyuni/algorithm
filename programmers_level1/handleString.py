def solution(s):
    if (4 == len(s) or len(s) == 6) and s.isnumeric():
        return True
    return False

print(solution("a234"))
print(solution("1234"))