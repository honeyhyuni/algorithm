# https://www.acmicpc.net/problem/2473
import sys
input = sys.stdin.readline
n = int(input())
arr = sorted(list(map(int, input().split())))
result = sys.maxsize
answer = []

for _ in range(n-2):
    left, right = _+1, n-1
    while left < right:
        temp = arr[left] + arr[right] + arr[_]
        if result > abs(temp):
            result = abs(temp)
            answer = [arr[_], arr[left], arr[right]]
        if temp == 0:
            print(arr[_], arr[left], arr[right])
            sys.exit()
        elif temp < 0:
            left += 1
        else:
            right -= 1
print(*answer)