# https://www.acmicpc.net/problem/9935
arr = list(map(str, input().rstrip()))
bomb = list(map(str, input().rstrip()))

temp = []

for i in range(len(arr)):
    temp.append(arr[i])
    if temp[-1] == bomb[-1] and len(temp) >= len(bomb):
        if temp[-len(bomb):] == bomb:
            for j in range(len(bomb)):
                temp.pop()
if temp:
    print("".join(temp))
else:
    print("FRULA")
