import sys
from collections import defaultdict

input = sys.stdin.readline
T = int(input())
for t in range(T):
    w = input().rstrip()
    k = int(input())
    dic = defaultdict(list)
    result = []
    for i in range(len(w)):
        dic[w[i]].append(i)
        if len(dic[w[i]]) == k:
            result.append(i - dic[w[i]][0] + 1)
            dic[w[i]].pop(0)
    print(min(result), max(result)) if result else print(-1)
