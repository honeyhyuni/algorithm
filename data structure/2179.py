# https://www.acmicpc.net/problem/2179
import sys
input = sys.stdin.readline
n = int(input())
ar = [[input().rstrip(), i] for i in range(n)]
result = [0] * n
arr = sorted(ar)
for i in range(n-1):
    s1, id1 = arr[i]
    s2, id2 = arr[i+1]
    c = 0
    for j in range(len(s1)):
        if s1[j] == s2[j]:
            c += 1
        else:
            break
    if c > 0:
        result[id1] = max(result[id1], c)
        result[id2] = max(result[id2], c)
t = 0
max_v = max(result)
for i in range(n):
    if t == 0:
        if result[i] == max_v:
            print(ar[i][0])
            t += 1
            temp = ar[i][0][:max_v]
    else:
        if result[i] == max_v and ar[i][0][:max_v] == temp:
            print(ar[i][0])
            break