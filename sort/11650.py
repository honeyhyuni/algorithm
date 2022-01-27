import sys
n = int(sys.stdin.readline())
a = []
for i in range(n):
    a.append(list(map(int, input().split())))

a.sort(key= lambda x: (x[0], x[1]))

for i in a:
    print(*i)
