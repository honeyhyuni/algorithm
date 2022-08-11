# https://www.acmicpc.net/problem/7490
import sys
from collections import deque
from itertools import product

input = sys.stdin.readline
T = int(input())
op = [" ", "+", "-"]


def check(a):
    q = deque(a)
    temp = []
    while q:
        x = q.popleft()
        if x == " ":
            temp[-1] = temp[-1] + q.popleft()
        else:
            temp.append(x)
    ans = int(temp[0])
    for i in range(1, len(temp) - 1, 2):
        if temp[i] == "+":
            ans += int(temp[i + 1])
        else:
            ans -= int(temp[i + 1])
    if ans == 0:
        return True
    return False


for t in range(T):
    n = int(input())
    o = list(product(op, repeat=n - 1))
    result = [0] * (n * 2 - 1)
    cnt = 1
    for i in range(0, n * 2 - 1, 2):
        result[i] = str(cnt)
        cnt += 1
    for i in o:
        cnt = 0
        for j in range(1, len(result) - 1, 2):
            result[j] = i[cnt]
            cnt += 1
        if check(result):
            print("".join(result))
    print()
