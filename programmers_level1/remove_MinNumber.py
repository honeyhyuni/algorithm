# https://programmers.co.kr/learn/courses/30/lessons/12935
def solution(arr):
    min_v = min(arr)
    arr.remove(min_v)
    if not arr:
        return [-1]
    return arr


solution([4, 3, 2, 1])
solution([10])