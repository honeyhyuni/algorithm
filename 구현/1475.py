# https://www.acmicpc.net/problem/1475
arr = list(map(int, input()))
result_arr = []
for i in range(10):
    result_arr.append(arr.count(i))
result_arr[6] += result_arr[9] # 6과 9 는 공유가능
result_arr[9] = 0

result_arr[6] = result_arr[6] // 2 + result_arr[6] % 2
print(max(result_arr))
