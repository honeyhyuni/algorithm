# https://www.acmicpc.net/problem/2822
import sys
input = sys.stdin.readline
arr = sorted([[int(input()), i+1] for i in range(8)])
sum_v, result = 0, []
for i, j in arr[3:]:
    sum_v += i
    result.append(j)
print(sum_v)
print(" ".join(sorted(map(str, result))))
