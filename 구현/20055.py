# https://www.acmicpc.net/problem/20055
import sys
from collections import deque
input = sys.stdin.readline
n, k = map(int, input().split())
q = deque(map(int, input().split()))
machine = deque([0] * n)
cnt = 0
while q.count(0) < k:
    q.rotate(1)
    machine.rotate(1)
    machine[-1] = 0
    if sum(machine): # 로봇이 하나라도 있을시
        for i in range(n-2, -1, -1): # 로봇 이동
            if machine[i] == 1 and machine[i+1] == 0 and q[i+1] >= 1:
                machine[i+1] = 1
                machine[i] = 0
                q[i+1] -= 1
        machine[-1] = 0
    if machine[0] == 0 and q[0] >= 1: # 로봇 올리기
        machine[0] = 1
        q[0] -= 1
    cnt += 1

print(cnt)
