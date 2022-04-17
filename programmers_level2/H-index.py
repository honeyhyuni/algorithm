# https://programmers.co.kr/learn/courses/30/lessons/42747
def solution(citations):
    citations.sort()
    for i, j in enumerate(citations):
        if j >= len(citations) - i:
            return len(citations) - i
    return 0


print(solution([3, 0, 6, 1, 5]))