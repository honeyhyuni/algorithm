# https://www.acmicpc.net/problem/17140
import sys

input = sys.stdin.readline
r, c, k = map(int, input().split())
arr = [list(map(int, input().split())) for i in range(3)]


def calculation():
    len_max = 0
    for i in range(len(arr)):
        temp = arr[i]
        dic = {}
        kkk = []
        for j in temp:
            dic[j] = temp.count(j)
        for s, d in dic.items():
            if s == 0:
                continue
            kkk.append([s, d])
        len_max = max(len(kkk), len_max)
        kkk.sort(key=lambda x: (x[1], x[0]))
        arr[i] = []
        for _, __ in kkk:
            arr[i].append(_)
            arr[i].append(__)
    for i in range(len(arr)):
        for j in range(len(arr[i]), len_max * 2):
            arr[i].append(0)


for i in range(101):
    if 0 <= r - 1 < len(arr) and 0 <= c - 1 < len(arr[0]) and arr[r - 1][c - 1] == k:
        print(i)
        sys.exit()
    if len(arr) >= len(arr[0]):
        calculation()
    else:
        arr = list(zip(*arr))
        calculation()
        arr = list(zip(*arr))
    arr = arr[:100][:100]
print(-1)
