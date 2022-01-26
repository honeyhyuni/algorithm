# https://www.acmicpc.net/problem/10814
n = int(input())
a = []

for _ in range(n):
    age, name = map(str, input().split())
    age = int(age)
    a.append((age, name))

a.sort(key = lambda x: x[0]) # 나이순으로 정렬

for i in a:
    print(i[0], i[1])