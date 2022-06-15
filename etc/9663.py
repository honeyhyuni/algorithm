# https://www.acmicpc.net/problem/9663
n = int(input())


def solution(n):
    global ans
    ans = 0
    arr = [0] * n
    back(arr, 0)
    return ans


def back(arr, x):
    global ans
    if x == len(arr):
        ans += 1
        return
    for i in range(len(arr)):
        arr[x] = i
        if check(arr, x):
            back(arr, x + 1)


def check(arr, x):
    for i in range(x):
        if arr[x] == arr[i] or abs(arr[x] - arr[i]) == abs(x - i):
            return False
    return True


print(solution(n))
