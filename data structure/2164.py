# https://www.acmicpc.net/problem/2164
import collections
n = int(input())
a = collections.deque([i for i in range(1, n+1)])

while len(a) > 1: # 맨앞장을 뽑아주고 반시계 방향으로 돌려준다
    a.popleft()
    a.rotate(-1)
print(a[0])