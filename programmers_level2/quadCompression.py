# https://programmers.co.kr/learn/courses/30/lessons/68936
def solution(arr):
    answer = [0, 0]
    n = len(arr)

    def back(x, y, n):
        temp = arr[x][y]
        for i in range(x, x+n):
            for j in range(y, y+n):
                if arr[i][j] != temp:
                    n //= 2
                    back(x, y, n)
                    back(x, y+n, n)
                    back(x+n, y, n)
                    back(x+n, y+n, n)
                    return
        answer[temp] += 1
    back(0, 0, n)
    return answer


print(solution([[1,1,0,0],[1,0,0,0],[1,0,0,1],[1,1,1,1]]))
print(solution([[1,1,1,1,1,1,1,1],[0,1,1,1,1,1,1,1],[0,0,0,0,1,1,1,1],[0,1,0,0,1,1,1,1],[0,0,0,0,0,0,1,1],[0,0,0,0,0,0,0,1],[0,0,0,0,1,0,0,1],[0,0,0,0,1,1,1,1]]))