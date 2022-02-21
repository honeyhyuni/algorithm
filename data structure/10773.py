# https://www.acmicpc.net/problem/10773
k = int(input())

a = []

for i in range(k):
    num = (int(input()))
    if num == 0:
        a.pop()
    else:
        a.append(num)
print(sum(a))