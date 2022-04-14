# https://programmers.co.kr/learn/courses/30/lessons/49994
def solution(dirs):
    dic = {"U": [-1, 0], "D": [1, 0], "R": [0, 1], "L": [0, -1]}
    visited = set()
    x, y = 0, 0
    for i in dirs:
        dx, dy = dic[i]
        nx = x + dx
        ny = y + dy
        if -5 <= nx <= 5 and -5 <= ny <= 5:
            visited.add((x, y, nx, ny))
            visited.add((nx, ny, x, y))
            x, y = nx, ny
    return len(visited) // 2

print(solution("ULURRDLLU"))
print(solution("LULLLLLLU"))