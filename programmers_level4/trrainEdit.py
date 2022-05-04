# https://programmers.co.kr/learn/courses/30/lessons/12984
def solution(land, P, Q):
    arr = []
    for i in land:
        arr += i
    arr.sort()
    n = len(arr)
    # 모든 칸을 제거 한 값
    answer = sum(arr) * Q
    # 가장 낮은 칸으로 모든 지형을 맞췄을때 값
    cost = (sum(arr) - arr[0] * n) * Q
    answer = min(answer, cost)
    for i in range(1, len(arr)):
        if arr[i] != arr[i-1]:
            cost += (arr[i] - arr[i-1]) * i * P - (arr[i] - arr[i-1]) * (n-i) * Q
        answer = min(answer, cost)
    return answer


print(solution([[1, 2], [2, 3]], 3, 2))
print(solution([[4, 4, 3], [3, 2, 2], [ 2, 1, 0 ]], 5, 3))