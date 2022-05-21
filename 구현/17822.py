import sys
from collections import deque

input = sys.stdin.readline
n, m, T = map(int, input().split())
arr = [[]]
for i in range(n):
    arr.append(deque(map(int, input().split())))


# 원판 회전
def rotate_circle(x, d, k):
    for i in range(1, n + 1):
        if i % x == 0:
            arr[i].rotate(d * k)


def ajd():
    delete = set()
    for i in range(1, n + 1):
        for j in range(m):
            if j == 0 and arr[i][j] != 0:  # 배열의 맨첫 원소일경우 마지막과 두번째 원소 비교
                for _ in [-1, 1]:
                    if arr[i][_] == arr[i][j]:
                        delete.update([(i, j), (i, _)])
            elif 0 < j < m - 1 and arr[i][j] != 0:  # 첫번째와 마지막 원소를 제외한 나머지 원소들 비교
                if arr[i][j] == arr[i][j + 1]:
                    delete.update([(i, j), (i, j + 1)])
            if 1 <= i < n and arr[i][j] != 0:  # 자신보다 하나 큰 원판과 같은 위치의 인덱스 비교
                if arr[i][j] == arr[i + 1][j]:
                    delete.update([(i, j), (i + 1, j)])
    if delete:
        for i, j in delete:
            arr[i][j] = 0
    else:
        if not avg_pm():
            return False
    return True


def avg_pm():
    zero_, len_ = 0, n * m
    sum_v = sum(map(sum, arr))
    if sum_v == 0:
        return False
    for i in arr:
        zero_ += i.count(0)
    avg_ = sum_v / (len_ - zero_)  # 평균
    for i in range(1, n + 1):
        for j in range(m):
            if arr[i][j] != 0:
                if arr[i][j] > avg_:
                    arr[i][j] -= 1
                elif arr[i][j] < avg_:
                    arr[i][j] += 1
    return True


for t in range(T):
    x, d, k = map(int, input().split())
    if d == 0:
        d = 1
    else:
        d = -1
    rotate_circle(x, d, k)
    if not ajd():
        break

print(sum(map(sum, arr)))
