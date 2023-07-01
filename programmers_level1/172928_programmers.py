# https://school.programmers.co.kr/learn/courses/30/lessons/172928
def solution(park, routes):
    answer = []
    n, m = len(park), len(park[0])
    dic = {"E": [0, 1], "S": [1, 0], "W": [0, -1], "N": [-1, 0]}

    for i in range(n):
        for j in range(m):
            if park[i][j] == "S":
                answer = [i, j]
                break
    for i in routes:
        dx, dy = dic[i[0]]
        dis = int(i[-1])
        for di in range(1, dis+1):
            nx, ny = answer[0] + (dx*di), answer[1] + (dy*di)
            if not (0 <= nx < n and 0 <= ny < m and park[nx][ny] != "X"):
                break
        else:
            answer = [nx, ny]
    return answer


print(solution(["SOO", "OOO", "OOO"], ["E 2", "S 2", "W 1"]))
print(solution(["SOO","OXX","OOO"], ["E 2","S 2","W 1"]))
