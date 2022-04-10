# https://programmers.co.kr/learn/courses/30/lessons/12948
def solution(phone_number):
    temp = ""
    for i in range(len(phone_number)-4):
        temp += "*"
    return temp + phone_number[-4:]


print(solution("01033334444"))
print(solution("027778888"))