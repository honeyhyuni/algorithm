# https://www.acmicpc.net/problem/10867
import sys
input = sys.stdin.readline
n = int(input())
arr = list(set(map(int, input().split())))  # 중복빼고 정렬이기 때문에 set 사용
arr.sort()

print(" ".join(map(str, arr)))