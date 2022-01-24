# https://www.acmicpc.net/problem/10820
import sys

while True:
    arr = sys.stdin.readline().rstrip('\n')
    result = [0] * 4

    if not arr:
        break
    for i in arr:
        if i.isupper():
            result[1] += 1
        elif i.islower():
            result[0] += 1
        elif i.isdigit():
            result[2] += 1
        elif i.isspace():
            result[3] += 1
    print(*result)