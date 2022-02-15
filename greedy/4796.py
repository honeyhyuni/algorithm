# https://www.acmicpc.net/problem/4796
i = 1
while True:
    L, P, V = map(int, input().split())
    if L == 0 and P == 0 and V == 0:
        break
    a = V // P
    b = min(V % P, L)
    print("Case " + str(i) + ": " + str(a * L + b))
    i += 1
