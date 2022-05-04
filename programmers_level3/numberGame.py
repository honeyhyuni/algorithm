# https://programmers.co.kr/learn/courses/30/lessons/12987
def solution(A, B):
    A.sort(reverse= True)
    B.sort(reverse= True)
    answer, idx = 0, 0
    for a in A:
        if a < B[idx]:
            answer += 1
            idx += 1
    return answer


print(solution([5, 1, 3, 7], [2, 2, 6, 8]))
print(solution([2, 2, 2, 2], [1, 1, 1, 1]))
