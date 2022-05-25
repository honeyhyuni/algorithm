# https://www.acmicpc.net/problem/2635
n = int(input())
result = []
for i in range(1, n+1):
    stack = [n, i]
    while True:
        v = stack[-2] - stack[-1]
        if v < 0:
            if len(stack) > len(result):
                result = stack
            break
        stack.append(v)
print(len(result))
print(*result)