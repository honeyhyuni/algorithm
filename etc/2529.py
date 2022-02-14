# https://www.acmicpc.net/problem/2529
n = int(input())
comp = list(map(str, input().split()))
st = ""
visited = [False] * 10
max_v = ""
min_v = ""


def check(i, j, k):
    if k == ">":
        return i > j
    else:
        return i < j


def back(cnt, s):
    global max_v, min_v
    if cnt > n:
        if len(min_v) == 0:
            min_v = s
        else:
            max_v = s
        return
    for i in range(10):
        if not visited[i]:
            if cnt == 0 or check(s[-1], str(i), comp[cnt-1]):
                visited[i] = True
                back(cnt+1, s + str(i))
                visited[i] = False
back(0, st)
print(max_v)
print(min_v)