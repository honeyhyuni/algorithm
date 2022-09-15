# https://www.acmicpc.net/problem/2467
import sys
input = sys.stdin.readline
n = int(input())
arr = sorted(list(map(int, input().split())))
left, right = 0, n-1
ans = sys.maxsize
answer = []
while left < right:
    temp = arr[left] + arr[right]
    if abs(temp) < ans:
        answer = [arr[left], arr[right]]
        ans = abs(temp)
    if temp == 0:
        answer = [arr[left], arr[right]]
        break
    elif temp < 0:
        left += 1
    else:
        right -= 1

print(*answer)