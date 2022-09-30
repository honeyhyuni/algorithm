# https://school.programmers.co.kr/learn/courses/30/lessons/120866
def solution(board):
    answer = 0
    dd = [(-1, -1), (-1, 0), (-1, 1), (0, 1), (1, 1), (1, 0), (1, -1), (0, -1)]
    n, m = len(board), len(board[0])
    temp = []
    for i in range(n):
        for j in range(m):
            if board[i][j] == 1:
                temp.append((i, j))
    for i, j in temp:
        for x, y in dd:
            nx = i + x
            ny = j + y
            if 0 <= nx < n and 0 <= ny < m:
                board[nx][ny] = 1
    for i in board:
        answer += i.count(0)
    return answer


print(solution([[0, 0, 0, 0, 0], [0, 0, 0, 0, 0], [0, 0, 0, 0, 0], [0, 0, 1, 0, 0], [0, 0, 0, 0, 0]]))