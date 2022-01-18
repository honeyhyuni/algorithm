# https://www.acmicpc.net/problem/2828
n, m = map(int, input().split())
j = int(input())
a = []

for i in range(j):
    a.append(int(input()))

end = m
start = 1
move = 0

for i in range(j):
    if start <= a[i] <= end:
        continue
    if a[i] >= end: # 사과의 위치가 바구니 크기 보다 오른쪽일 경우
        move += a[i] - end
        end = a[i]
        start = end - m + 1
    else: # 사과의 위치가 바구니 크기 보다 왼쪽일 경우
        move += start - a[i]
        start = a[i]
        end = start + m - 1
print(move)
