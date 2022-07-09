# https://www.acmicpc.net/problem/1092
import sys
input = sys.stdin.readline
n = int(input())
crane = list(map(int, input().split()))
m = int(input())
box = list(map(int, input().split()))
# 크레인으로 화물을 옮길수 없다면 -1 출력
if max(box) > max(crane):
    print(-1)
else:
    cnt = 0
    crane.sort(reverse=True)
    box.sort(reverse=True)
    while box:
        for c in crane:
            if not box:
                break
            for b in box:
                if c >= b:
                    box.remove(b)
                    break
        cnt += 1

    print(cnt)
