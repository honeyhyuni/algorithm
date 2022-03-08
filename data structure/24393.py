# https://www.acmicpc.net/problem/24393
import sys
input = sys.stdin.readline
n = int(input())
q = [i for i in range(1, 28)]

for __ in range(n):
    arr = list(map(int, input().split()))
    left = q[0:13] # 왼쪽카드
    right = q[13:28] # 오른쪽카드
    q = []
    for i in range(len(arr)):
        if i % 2 == 0:
            for _ in range(arr[i]):
                q.append(right[0])
                right.pop(0)
        else:
            for _ in range(arr[i]):
                q.append(left[0])
                left.pop(0)
print(q.index(1)+1)