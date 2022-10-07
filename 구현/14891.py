# https://www.acmicpc.net/problem/14891
import sys
from collections import deque

input = sys.stdin.readline


def rotate_right(a, b):
    if a > 4 or arr[a - 1][2] == arr[a][6]:
        return
    if arr[a - 1][2] != arr[a][6]:
        rotate_right(a + 1, -b)
        arr[a].rotate(b)


def rotate_left(a, b):
    if a < 1 or arr[a][2] == arr[a + 1][6]:
        return
    if arr[a][2] != arr[a + 1][6]:
        rotate_left(a - 1, -b)
        arr[a].rotate(b)


arr = {}
for i in range(1, 5):
    arr[i] = deque(list(map(int, input().rstrip())))

k = int(input())
for i in range(k):
    a, b = map(int, input().split())
    rotate_right(a + 1, -b)
    rotate_left(a - 1, -b)
    arr[a].rotate(b)

result = 0
for i in range(4):
    result += (2 ** i) * arr[i+1][0]

print(result)