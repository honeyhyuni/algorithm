# https://www.acmicpc.net/problem/13417
from collections import deque
import sys
input = sys.stdin.readline
t = int(input())
for _ in range(t):
    n = int(input())
    arr = list(map(str, input().split()))

    result = deque()
    result.append(arr[0])
    for i in range(1, n):
        if arr[i] <= result[0]: # 사전순으로 맨앞글자보다 작다면 맨앞에 삽입
            result.appendleft(arr[i])
        else:                   # 아닐경우 맨뒤에 삽입
            result.append(arr[i])

    print(''.join(result))
