# https://www.acmicpc.net/problem/1652
import sys

input = sys.stdin.readline
n = int(input())
arr = []
for i in range(n):
    arr.append(list(map(str, input().rstrip())))


def check():
    result = 0
    for i in arr:
        cnt = 0
        for j in i:
            if j == ".":
                cnt += 1
            else:
                if cnt >= 2:
                    result += 1
                cnt = 0
        if cnt >= 2:
            result += 1
    return result


print(check(), end=' ')
arr = zip(*arr)
print(check())
