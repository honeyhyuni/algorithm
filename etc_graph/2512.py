# https://www.acmicpc.net/problem/2512
n = int(input())
a = list(map(int, input().split()))
m = int(input())

a.sort()

start , end = 0, max(a)
while start <= end: # 이분탐색
    num = 0
    mid = (start + end) // 2
    for i in a:
        if i >= mid:
            num += mid
        else:
            num += i
    if num <= m:
        start = mid + 1
    else:
        end = mid - 1

print(end)

