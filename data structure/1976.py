# https://www.acmicpc.net/problem/1976
# union- find
import sys

sys.setrecursionlimit(10 ** 5)
input = sys.stdin.readline
n = int(input())
m = int(input())
arr = [i for i in range(n + 1)]


def find_parent(var):
    if var != arr[var]:
        arr[var] = find_parent(arr[var])
    return arr[var]


for i in range(1, n + 1):
    t = list(map(int, input().split()))
    for j in range(len(t)):
        if i == j + 1:
            continue
        if t[j] == 1:
            i_n = find_parent(i)
            j_n = find_parent(j+1)
            if i_n != j_n:
                if i_n < j_n:
                    arr[j_n] = i_n
                else:
                    arr[i_n] = j_n

node = sorted(list(map(int, input().split())))

result = set()
for i in node:
    result.add(arr[i])
print("YES" if len(result) == 1 else "NO")
