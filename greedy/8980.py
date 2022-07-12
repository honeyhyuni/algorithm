# https://www.acmicpc.net/problem/8980
import sys
input = sys.stdin.readline
n, m = map(int, input().split())
T = int(input())
arr = []
for i in range(T):
    arr.append(list(map(int, input().split())))
# 도착지점 기준 오름차순 정렬
arr.sort(key= lambda x:x[1])
box = [m] * (n+1)
result = 0

# 최소값 계속 갱신해주면서 더해준다.
for start, end, value in arr:
    min_v = m
    for i in range(start,end):
        min_v = min(min_v, box[i])
    min_v = min(min_v, value)
    for i in range(start, end):
        box[i] -= min_v
    result += min_v
print(result)