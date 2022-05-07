# https://www.acmicpc.net/problem/1747
n = int(input())
result = 0
for i in range(n, 1000001):
    if i == 1:
        continue
    for j in range(2, int(i ** 0.5)+1):
        if i % j == 0:
            break
    else:
        if str(i) == str(i)[::-1]:
            result = i
            break
if result == 0:
    result = 1003001
print(result)
