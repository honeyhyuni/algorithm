# https://www.acmicpc.net/problem/25184
n = int(input())
if n == 1:
    print(1)
else:
    v = n // 2
    plus, minus = n//2, n//2+1
    result = [v]
    while len(result) < n:
        if v > minus:
            v -= minus
        else:
            v += plus
        result.append(v)
    print(*result)