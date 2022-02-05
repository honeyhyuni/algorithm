# https://www.acmicpc.net/problem/1541
arr = input().split("-")
num = []
for i in arr:
    result = 0
    s = i.split("+")
    for j in s:
        result += int(j)
    num.append(result)
n = num[0]
for i in range(1, len(num)):
    n -= num[i]
print(n)