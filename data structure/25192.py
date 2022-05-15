# https://www.acmicpc.net/problem/25192
import sys
input = sys.stdin.readline
n = int(input())
check = set()
result = 0
for i in range(n):
    x = input().rstrip()
    if x == "ENTER":
        result += len(check)
        check.clear()
    else:
        check.add(x)
print(result+len(check))