# https://programmers.co.kr/learn/courses/30/lessons/77484
def solution(lottos, win_nums):
    rank = [6, 6, 5, 4, 3, 2, 1]
    answer = []
    result = 0
    for i in lottos:
        result += win_nums.count(i)
    M = result + lottos.count(0)
    answer.append([rank[M], rank[result]])
    return answer


print(solution([44, 1, 0, 0, 31, 25], [31, 10, 15, 1, 6, 19]))
