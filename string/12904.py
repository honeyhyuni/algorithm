# https://www.acmicpc.net/problem/12904
import sys
input = sys.stdin.readline

s = list(map(str, input().rstrip()))
t = list(map(str, input().rstrip()))

for i in range(len(t)-1, -1, -1):
    if s == t:
        print(1)
        break
    else:
        if t[i] == "A":
            t.pop(i)
        else:
            t.pop(i)
            t = t[::-1]
if not t:
    print(0)





