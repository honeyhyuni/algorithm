# https://www.acmicpc.net/problem/1934
import math
import sys
input = sys.stdin.readline
T = int(input())
for t in range(T):
    x, y = map(int, input().split())
    print(x*y // math.gcd(x, y))