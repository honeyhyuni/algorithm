# https://www.acmicpc.net/problem/1343
n = input()

n = n.replace("XXXX", "AAAA")
n = n.replace("XX", "BB")

if "X" in n:
    print(-1)
else:
    print(n)