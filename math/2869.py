# https://www.acmicpc.net/problem/2869
import math
a, b, v = map(int, input().split())
print(math.ceil((v-b) / (a-b)))