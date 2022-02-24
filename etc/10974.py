# https://www.acmicpc.net/problem/10974
n = int(input())
arr = []


def back():
    if len(arr) == n:
        print(' '.join(map(str, arr)))
        return

    for i in range(1, n + 1):
        if i not in arr:
            arr.append(i)
            back()
            arr.pop()


back()
