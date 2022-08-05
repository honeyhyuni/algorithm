# https://www.acmicpc.net/problem/25330
import sys

input = sys.stdin.readline
n, k = map(int, input().split())
attack = list(map(int, input().split()))
score = list(map(int, input().split()))

max_v = 0


def back(energy, idx, sco):
    global max_v
    temp = energy - sum(attack[i] for i in idx)
    if temp >= 0:
        max_v = max(max_v, sco)
    if temp <= 0:
        return
    for j in range(n):
        if not visited[j]:
            visited[j] = True
            back(temp, idx + [j], sco + score[j])
            visited[j] = False


for i in range(n):
    visited = [False] * n
    visited[i] = True
    back(k, [i], score[i])

print(max_v)
