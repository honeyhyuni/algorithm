# https://programmers.co.kr/learn/courses/30/lessons/12947
def solution(x):
    temp = 0
    for i in str(x):
        temp += int(i)
    return True if x % temp == 0 else False



print(solution(10))
print(solution(12))
print(solution(11))
print(solution(13))