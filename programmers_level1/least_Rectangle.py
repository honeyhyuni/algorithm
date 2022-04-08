# https://programmers.co.kr/learn/courses/30/lessons/86491
def solution(sizes):
    min_v, max_v = 0, 0
    for i in sizes:
        max_v = max(max_v, max(i))
        min_v = max(min_v, min(i))
    return max_v * min_v


print(solution([[60, 50], [30, 70], [60, 30], [80, 40]]))
print(solution([[10, 7], [12, 3], [8, 15], [14, 7], [5, 15]]))
print(solution([[14, 4], [19, 6], [6, 16], [18, 7], [7, 11]]))
