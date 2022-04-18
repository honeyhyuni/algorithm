# https://programmers.co.kr/learn/courses/30/lessons/17679
from collections import deque


def solution(n, m, board):
    answer = 0
    while True:
        q = deque()
        for i in range(n):
            board[i] = list(map(str, board[i]))
        for i in range(n - 1):
            for j in range(m - 1):
                if board[i][j] == " ":
                    continue
                if board[i][j] == board[i + 1][j] == board[i][j + 1] == board[i + 1][j + 1]:
                    for _ in [[i, j], [i + 1, j], [i, j + 1], [i + 1, j + 1]]:
                        if _ not in q:
                            q.append(_)
        if not q:
            break
        while q:
            x, y = q.popleft()
            board[x][y] = " "
            answer += 1

        for i in range(m):
            for j in range(n - 1, -1, -1):
                if board[j][i] != " ":
                    q.append(board[j][i])

            for j in range(n - 1, -1, -1):
                if q:
                    board[j][i] = q.popleft()
                else:
                    board[j][i] = " "
    return answer


print(solution(4, 5, ["CCBDE", "AAADE", "AAABF", "CCBBF"]))
