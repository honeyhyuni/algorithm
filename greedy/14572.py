# https://www.acmicpc.net/problem/14572
import sys

input = sys.stdin.readline
n, k, D = map(int, input().split())
lst = []
for i in range(n):
    m, d = map(int, input().split())
    t = list(map(int, input().split()))
    lst.append((m, d, t))
lst.sort(key=lambda x: x[1])

max_v = 0
left, right = 0, 1
total, now = len(lst[0][2]), 0

score = [0] * (k + 1)
for i in lst[0][2]:
    score[i] += 1


# 모두 아는 알고리즘 수 return
def check(left, right):
    temp, now = right - left + 1, 0
    for i in range(1, k+1):
        if score[i] == temp:
            now += 1
    return now


# 엄청 까다롭진 않은 두 포인터
while right < n:
    if lst[right][1] - lst[left][1] <= D:
        for i in lst[right][2]:
            score[i] += 1
            if score[i] == 1:
                total += 1
        now = check(left, right)
        max_v = max(max_v, (total - now) * (right - left + 1))
        right += 1
    else:
        for i in lst[left][2]:
            score[i] -= 1
            if score[i] == 0:
                total -= 1
        left += 1

print(max_v)
