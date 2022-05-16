# https://www.acmicpc.net/problem/6588
visited = [True] * 1000001
for i in range(2, 1001):
    if visited[i]:
        for j in range(i + i, len(visited), i):
            visited[j] = False

while True:
    x = int(input())
    if x == 0:
        break
    for i in range(3, x//2+1):
        if visited[i] and visited[x-i]:
            print("%d = %d + %d" % (x, i, x-i))
            break
    else:
        print("Goldbach's conjecture is wrong.")
