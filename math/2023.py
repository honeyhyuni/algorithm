# https://www.acmicpc.net/problem/2023
n = int(input())
arr = [i for i in range(10)]

result = []


def dfs(num):
    if len(str(num)) == n:
        print(num)
        return
    for i in range(10):
        temp = num * 10 + i
        if check(temp):
            dfs(temp)


def check(a):
    if a < 2:
        return False
    for j in range(2, int(a ** 0.5) + 1):
        if a % j == 0:
            return False
    return True


dfs(2)
dfs(3)
dfs(5)
dfs(7)
