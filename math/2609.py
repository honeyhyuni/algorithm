# https://www.acmicpc.net/problem/2609
import math

n, m = map(int, input().split())

gcd_v = math.gcd(n, m)

print(gcd_v)
print(n*m // gcd_v)