# https://www.acmicpc.net/problem/1062
import sys
from itertools import combinations
input = sys.stdin.readline

n, k = map(int, input().split())
if k < 5:
    print(0)
else:
    dic = list(set(input().rstrip()[4:-4]) for i in range(n))
    icy_word = {'a', 'n', 't', 'i', 'c'}
    teach = set(chr(i + 97) for i in range(26))
    teach -= icy_word
    result = 0
    visited = [0] * 26
    for i in icy_word:
        visited[ord(i) - 97] = 1
    for i in dic:
        i -= icy_word
    for i in list(combinations(teach, k-5)):
        temp = 0
        for j in i:
            visited[ord(j)-97] = 1
        for j in dic:
            for k in j:
                if visited[ord(k) - 97] == 0:
                    break
            else:
                temp += 1
        for j in i:
            visited[ord(j)-97] = 0
        result = max(result, temp)
    print(result)