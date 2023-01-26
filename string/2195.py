# https://www.acmicpc.net/problem/2195
s = input().rstrip()
p = list(map(str, input().rstrip()))

temp, cnt = "", 0
while p:
    x = p.pop(0)
    if temp + x not in s:
        cnt += 1
        temp = x
    else:
        temp += x

print(cnt+1)