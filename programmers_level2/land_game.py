# https://programmers.co.kr/learn/courses/30/lessons/12913
def solution(land):
    for i in range(1, len(land)):
        for j in range(4):
            max_v = -1
            for k in range(4):
                if j == k:
                    continue
                max_v = max(max_v, land[i-1][k])
            land[i][j] += max_v

    return max(land[-1])


print(solution([[1,2,3,5],[5,6,7,8],[4,3,2,1]]))