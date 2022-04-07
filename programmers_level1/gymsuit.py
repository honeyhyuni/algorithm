# https://programmers.co.kr/learn/courses/30/lessons/42862
def solution(n, lost, reserve):
    s_lost = set(lost) - set(reserve)
    s_reserve = set(reserve) - set(lost)

    for i in s_reserve:
        if i-1 in s_lost:
            s_lost.remove(i-1)
        elif i+1 in s_lost:
            s_lost.remove(i+1)
    return n-len(s_lost)