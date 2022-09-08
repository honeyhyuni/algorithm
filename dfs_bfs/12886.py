# https://www.acmicpc.net/problem/12886
import copy
from itertools import combinations
from collections import deque
arr = list(map(int, input().split()))
com = list(combinations(range(3), 2))
q = deque([sorted(arr)])
visited = set()
visited.add(tuple(sorted(arr)))
if sum(arr) % 3 != 0:
    print(0)
else:
    while q:
        a = q.popleft()
        if a[0] == a[1] == a[2]:
            print(1)
            break
        for i, j in com:
            temp = copy.deepcopy(a)
            if a[i] == a[j]:
                continue
            temp[i] += a[i]
            temp[j] -= a[i]
            temp.sort()
            if tuple(temp) not in visited:
                visited.add(tuple(temp))
                q.append(temp)
    else:
        print(0)