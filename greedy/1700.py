# https://www.acmicpc.net/problem/1700
import sys

input = sys.stdin.readline
n, m = map(int, input().split())
arr = list(map(int, input().split()))

plug = []
result = 0
while arr:
    v = arr.pop(0)
    if v in plug:
        continue
    elif len(plug) == n:
        temp = []
        for i in range(len(plug)):
            try:
                temp.append(arr.index(plug[i]))
            except:
                #  plug 에 꽂혀있는 전기용품이
                #  후에 사용해야할 arr 리스트 안에 없다면
                #  뽑아버림
                plug.pop(i)
                result += 1
                break
        else:
            # 전부 또 재사용된다면 가장 늦게 사용될 예정일
            # 플러그를 뽑아버림
            plug.pop(plug.index(arr[max(temp)]))
            result += 1
    plug.append(v)
print(result)
