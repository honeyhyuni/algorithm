# https://programmers.co.kr/learn/courses/30/lessons/64061
from collections import deque


def solution(board, moves):
    answer = 0
    q = deque()
    for y in moves:
        y -= 1
        for x in range(len(board)):
            if board[x][y] != 0:
                if q and q[-1] == board[x][y]:
                    q.pop()
                    answer += 2
                else:
                    q.append(board[x][y])
                board[x][y] = 0
                break
    return answer
