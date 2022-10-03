# https://www.acmicpc.net/problem/25709
n = list(input().rstrip())
cnt = 0
while "1" in n:
    n.pop(n.index("1"))
    cnt += 1
while n and int("".join(n)) != 0:
    x = int(n.pop())
    if x == 0:
        cnt += 9
    else:
        cnt += x
print(cnt)