# https://www.acmicpc.net/problem/1339
import sys

input = sys.stdin.readline

n = int(input())
arr = [list(input().rstrip()) for i in range(n)]

dic = {}

for i in arr:
    len_ = len(i) - 1
    for j in i:
        if j in dic:
            dic[j] += 10 ** len_
        else:
            dic[j] = 10 ** len_
        len_ -= 1
dic = sorted(dic.values(), reverse=True)
result, cnt = 0, 9
for i in dic:
    result += cnt * i
    cnt -= 1
print(result)