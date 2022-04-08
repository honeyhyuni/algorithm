# https://programmers.co.kr/learn/courses/30/lessons/12917
def solution(s):
    answer = ''
    arr = []
    for i in s:
        arr.append(ord(i))
    arr.sort(reverse=True)
    for i in arr:
        answer += chr(i)
    return answer


print(solution("Zbcdefg"))
