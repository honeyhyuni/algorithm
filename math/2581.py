# https://www.acmicpc.net/problem/2581
a = int(input())
b = int(input())
result = []
for i in range(a, b+1):
    if i == 1:
        continue
    for j in range(2, int(i**0.5)+1):
        if i % j == 0:
            break
    else:
        result.append(i)
if not result:
    print(-1)
else:
    print(sum(result))
    print(result[0])