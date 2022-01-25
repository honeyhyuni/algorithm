# https://www.acmicpc.net/problem/1158
n, k = map(int, input().split())
arr = [i for i in range(1, n+1)]

idx = 0
result = []
for i in range(n):
    idx += k-1
    if idx >= len(arr):
        idx %= len(arr)
    result.append(arr.pop(idx))


print("<", ", ".join(map(str, result)), ">", sep='')
