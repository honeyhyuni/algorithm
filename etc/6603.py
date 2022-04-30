# https://www.acmicpc.net/status?user_id=tjfkqwkd001&problem_id=6603&from_mine=1
from itertools import combinations
import sys
input = sys.stdin.readline
while True:
    arr = list(map(int, input().split()))
    if arr[0] == 0:
        break
    lst = list(combinations(arr[1:], 6))
    for i in lst:
        print(*i)
    print()