# https://www.acmicpc.net/problem/2108
import sys
from collections import Counter

input = sys.stdin.readline
arr = []
n = int(input())
for i in range(n):
    arr.append(int(input()))
arr.sort()

if n == 1:
    print(arr[0])
    print(arr[0])
    print(arr[0])
    print(0)
    sys.exit()

print(round(sum(arr)/n)) # 산술평균
print(arr[n//2]) #중앙값

cnt = Counter(arr).most_common() 
print(cnt)

if cnt[0][1] == cnt[1][1]: # 최빈값
    print(cnt[1][0])
else:
    print(cnt[0][0])

print(arr[-1] - arr[0]) # 범위