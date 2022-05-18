# https://www.acmicpc.net/problem/16922

n = int(input())
arr = [1, 5, 10, 50]
ans = []
result = set()


def back(idx):
    if len(ans) == n:
        result.add(sum(ans))
        return
    for i in range(idx, len(arr)):
        ans.append(arr[i])
        back(i)
        ans.pop()


back(0)
print(len(result))
