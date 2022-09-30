# https://school.programmers.co.kr/learn/courses/30/lessons/120883
def solution(id_pw, db):
    if id_pw in db:
        return "login"
    for i in db:
        if i[0] == id_pw[0]:
            return "wrong pw"
    return "fail"


print(solution(["meosseugi", "1234"], [["rardss", "123"], ["yyoom", "1234"], ["meosseugi", "1234"]]))
print(solution(["programmer01", "15789"], [["programmer02", "111111"], ["programmer00", "134"], ["programmer01", "1145"]]))
print(solution(["rabbit04", "98761"], [["jaja11", "98761"], ["krong0313", "29440"], ["rabbit00", "111333"]]))