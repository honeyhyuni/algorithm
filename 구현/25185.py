# https://www.acmicpc.net/problem/25185
import sys
from collections import defaultdict

input = sys.stdin.readline
T = int(input())
for t in range(T):
    arr = sorted(list(map(str, input().split())))
    if arr[0] == arr[1] and arr[2] == arr[3]:
        print(":)")
        continue
    dic = defaultdict(list)
    for i in arr:
        dic[i[1]].append(int(i[0]))
    bol = False
    for i in dic.values():
        if len(i) >= 3:
            stack_one, stack_two = [i[0]], [i[0]]
            for j in range(1, len(i)):
                if i[j] != stack_one[-1]:
                    if i[j] - stack_one[-1] != 1:
                        stack_one.clear()
                    stack_one.append(i[j])
                if i[j] != stack_two[-1]:
                    stack_two.clear()
                stack_two.append(i[j])
                if len(stack_one) == 3 or len(stack_two) == 3:
                    bol = True
                    print(":)")
                    break
            if bol:
                break
    if not bol:
        print(":(")

