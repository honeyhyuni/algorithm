# https://www.acmicpc.net/problem/1213
import sys

arr = list(map(str,input()))

al = [0] * 26

for i in arr:
    al[ord(i) - 65] += 1

cnt = 0
result = ''
mid = ''
for i in range(26):
    if al[i] % 2 == 1:
        cnt += 1
        mid += chr(i+65)
    result += chr(i+65) * (al[i] // 2)
    if cnt > 1:
        print("I'm Sorry Hansoo")
        sys.exit()
print(result+mid+result[::-1])