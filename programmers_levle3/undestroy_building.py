# https://programmers.co.kr/learn/courses/30/lessons/92344
def solution(board, skill):
    answer = 0
    n, m = len(board), len(board[0])
    temp = [[0 for i in range(m + 1)] for i in range(n + 1)]
    # 누적합을 위한 범위 지정
    for ty, x1, y1, x2, y2, v in skill:
        if ty == 1:
            temp[x1][y1] -= v
            temp[x1][y2 + 1] += v
            temp[x2 + 1][y1] += v
            temp[x2 + 1][y2 + 1] -= v
        else:
            temp[x1][y1] += v
            temp[x1][y2 + 1] -= v
            temp[x2 + 1][y1] -= v
            temp[x2 + 1][y2 + 1] += v

    # 행 누적합
    for i in range(len(temp)-1):
        for j in range(len(temp[0])-1):
            temp[i+1][j] += temp[i][j]

    # 열 누적합
    for i in range(len(temp)-1):
        for j in range(len(temp[0])-1):
            temp[i][j+1] += temp[i][j]

    # #  누적합 다른 방법
    # for i in range(1, len(temp)):
    #     temp[i][0] += temp[i-1][0]
    # for i in range(1, len(temp)):
    #     temp[0][i] += temp[0][i-1]
    # for i in range(1, len(temp)):
    #     for j in range(1, len(temp[0])):
    #         temp[i][j] += temp[i][j - 1] + temp[i - 1][j] - temp[i - 1][j - 1]
    for i in range(n):
        for j in range(m):
            if board[i][j] + temp[i][j] > 0:
                answer += 1

    return answer


print(solution([[5, 5, 5, 5, 5], [5, 5, 5, 5, 5], [5, 5, 5, 5, 5], [5, 5, 5, 5, 5]],
               [[1, 0, 0, 3, 4, 4], [1, 2, 0, 2, 3, 2], [2, 1, 0, 3, 1, 2], [1, 0, 1, 3, 3, 1]]))
print(solution([[1, 2, 3], [4, 5, 6], [7, 8, 9]], [[1, 1, 1, 2, 2, 4], [1, 0, 0, 1, 1, 2], [2, 2, 0, 2, 0, 100]]))
