# https://programmers.co.kr/learn/courses/30/lessons/72410
def solution(new_id):
    temp = ["-", "_", "."]
    new_id = new_id.lower()
    answer = ""
    for i in new_id:
        if i.isalpha() or i in temp or i.isdigit():
            answer += i

    while ".." in answer:
        answer = answer.replace("..", ".")
    if len(answer) >= 2:
        if answer[0] == ".":
            answer = answer[1:]
        if answer[-1] == ".":
            answer = answer[:-1]
    else:
        if answer == ".":
            answer = ""
    if answer == "":
        answer = "a"
    answer = answer[:15]
    if answer[-1] == ".":
        answer = answer[:-1]

    while len(answer) < 3:
        answer += answer[-1]
    return answer


print(solution("...!@BaT#*..y.abcdefghijklm"))
print(solution("z-+.^."))
print(solution("=.="))
print(solution("123_.def"))
print(solution("abcdefghijklmn.p"))