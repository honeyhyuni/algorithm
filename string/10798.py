# https://www.acmicpc.net/problem/10798
a = []

for i in range(5):
    a.append(list(map(str, input())))

# 각 문자열마다 길이가 달라 최대 글자수인 15개의 크기만큼 False 추가
for i in range(5):
    for j in range(len(a[i]), 15):
        a[i].append(False)

for i in range(15):
    for j in range(5):
        if a[j][i]:
            print(a[j][i], end='')
