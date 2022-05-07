# https://www.acmicpc.net/problem/1764
n, m = map(int, input().split())
dic = {}
for i in range(n+m):
    x = input()
    if x in dic:
        dic[x] += 1
    else:
        dic[x] = 1
cnt = 0
result = []
for i in dic.keys():
    if dic[i] == 2:
        result.append(i)
print(len(result))
print("\n".join(sorted(result)))
