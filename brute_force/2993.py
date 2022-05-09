# https://www.acmicpc.net/problem/2993
s = list(map(str, input().rstrip()))
result = []
for i in range(1, len(s)-1):
    for j in range(i+1, len(s)):
        result.append(s[:i][::-1]+s[i:j][::-1]+s[j:][::-1])
print("".join(min(result)))