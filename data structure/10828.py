# https://www.acmicpc.net/problem/10828
import sys
n = int(sys.stdin.readline())
a = []
for i in range(n):
    i = sys.stdin.readline().split()
    if i[0] == "pop":
        if not a:
            print(-1)
        else:
            b = a.pop()
            print(b)
    elif i[0] == "size":
        b = len(a)
        print(b)
    elif i[0] == "empty":
        if not a:
            print(1)
        else:
            print(0)
    elif i[0] == "top":
        if not a:
            print(-1)
        else:
            b = a.pop()
            print(b)
            a.append(b)
    else:
        a.append(i[1])




