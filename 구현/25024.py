# https://www.acmicpc.net/problem/25024
import sys
input = sys.stdin.readline
n = int(input())
for i in range(n):
    result = []
    x, y = map(int, input().split())
    result.append("Yes") if 0 <= x <= 23 and 0 <= y <= 59 else result.append("No")
    result.append("Yes") if (x in [1, 3, 5, 7, 8, 10, 12] and 1 <= y <= 31) or (x in [4, 6, 9, 11] and 1 <= y <= 30) or (x == 2 and 1 <= y <= 29) else result.append("No")
    print(" ".join(result))