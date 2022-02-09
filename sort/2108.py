# https://www.acmicpc.net/problem/2108
import sys
n = int(sys.stdin.readline())
a = []

result = [0 for _ in range(10001)]
for i in range(n):
    num = int(sys.stdin.readline())
    result[num] += 1

for i in range(len(result)):
    for j in range(result[i]):
        print(i)






