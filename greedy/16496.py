# https://www.acmicpc.net/problem/16496
n = int(input())
numbers = sorted(list(map(str, input().split())), key=lambda x: x*9, reverse=True)
print(int("".join(numbers)))