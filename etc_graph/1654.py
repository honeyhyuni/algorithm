# https://www.acmicpc.net/problem/1654
n, k = map(int, input().split())
a = []
for i in range(n):
    a.append(int(input()))

start = 1
end = max(a)

while start <= end: # 이분탐색
    mid = (start + end)//2
    cnt = 0
    for i in a:
        cnt += i//mid
    if cnt >= k:
        start = mid + 1
    else:
        end = mid - 1

print(end)