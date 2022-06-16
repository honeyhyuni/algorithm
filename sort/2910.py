# https://www.acmicpc.net/problem/2910
import sys
from collections import Counter
input = sys.stdin.readline
n, m = map(int, input().split())
arr = list(map(int, input().split()))
a = Counter(arr).most_common()
for i, j in a:
    print((str(i) + ' ') * j, end='')