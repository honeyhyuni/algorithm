# https://www.acmicpc.net/problem/10971
from itertools import permutations
import sys

input = sys.stdin.readline
n = int(input())
arr = [list(map(int, input().split())) for i in range(n)]
lst_ = [i for i in range(n)]
lst = list(permutations(lst_))
result = sys.maxsize
for i in lst:
    i = list(i) + [i[0]]  # 모든 n개 도시를 방문후 처음으로 돌아가야함
    temp = 0
    for j in range(n):
        if arr[i[j]][i[j + 1]] == 0:  # 길 유무 확인
            break
        temp += arr[i[j]][i[j + 1]]
    else:
        result = min(result, temp)
print(result)
