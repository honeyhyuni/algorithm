# https://www.acmicpc.net/problem/10423
import sys

input = sys.stdin.readline
n, m, k = map(int, input().split())
yny = list(map(int, input().split()))


node = []
for i in range(m):
    x, y, z = map(int, input().split())
    node.append([x, y, z])
    node.append([y, x, z])
node.sort(key=lambda x: x[2])


def find_parent(var):
    if var != arr[var]:
        arr[var] = find_parent(arr[var])
    return arr[var]


result = 0

# 두개의 노드가 들어왔을때 하나의 노드의 부모가 yny 에 있는 노드라면
# 부모 노드를 yny 노드로 최신화 해주는 방버

# arr = [i for i in range(n + 1)]
# for a, b, c in node:
#     a_n = find_parent(a)
#     b_n = find_parent(b)
#     if a_n != b_n:
#         if a_n in yny and b_n in yny:
#             continue
#         if a_n in yny or b_n in yny:
#             for i in range(len(yny)):
#                 if a_n == yny[i]:
#                     arr[b_n] = yny[i]
#                     break
#                 if b_n == yny[i]:
#                     arr[a_n] = yny[i]
#                     break
#         elif a_n < b_n:
#             arr[b_n] = a_n
#         else:
#             arr[a_n] = b_n
#         result += c

# 초기에 yny 에 있는 노드의 부모 노드를 0 으로 초기화하는 방법
arr = [0] * (n+1)
for i in range(1, n+1):
    if i in yny:
        continue
    arr[i] = i
for a, b, c in node:
    a_n = find_parent(a)
    b_n = find_parent(b)
    if a_n != b_n:
        if a_n < b_n:
            arr[b_n] = a_n
        else:
            arr[a_n] = b_n
        result += c


print(result)
