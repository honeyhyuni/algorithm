# https://www.acmicpc.net/problem/1181
n = int(input())
arr = []
for i in range(n):
    arr.append(input())

result = list(set(arr)) # 같은 단어가 여러번 입력된 경우 한번씩만 출력 해야함
result.sort(key= lambda x: (len(x), x))

print("\n".join(result))
