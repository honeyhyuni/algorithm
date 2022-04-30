# https://www.acmicpc.net/problem/2529
import sys
input = sys.stdin.readline

n = int(input())
compare = list(map(str, input().split()))
arr = []


def check():
    if len(arr) >= 2:
        if compare[len(arr) - 2] == "<":
            if arr[-2] > arr[-1]:
                return False
        else:
            if arr[-2] < arr[-1]:
                return False
    if len(arr) == n + 1:
        result.append("".join(map(str, arr)))
        return False
    return True


result = []


def back():
    for i in range(10):
        if i in arr:
            continue
        arr.append(i)
        if check():
            back()
        arr.pop()


back()
print(result[-1])
print(result[0])
