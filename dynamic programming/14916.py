# https://www.acmicpc.net/problem/14916
n = int(input())

result = 0

while True:
    if n < 0:
        result = -1
        break
    if n % 5 == 0:
        result += n // 5
        break
    else:
        n -= 2
        result += 1

print(result)
