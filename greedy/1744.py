import sys
input = sys.stdin.readline
n = int(input())
plus_arr = []
minus_arr = []
one_arr = []
for i in range(n):
    num = int(input())
    if num > 1:
        plus_arr.append(num)
    elif num <= 0:
        minus_arr.append(num)
    else:
        one_arr.append(num)
result = 0
plus_arr.sort(reverse = True)
minus_arr.sort()
if len(plus_arr) % 2 == 0:
    for i in range(0, len(plus_arr), 2):
        result += plus_arr[i] * plus_arr[i + 1]
else:
    for i in range(0, len(plus_arr)-1, 2):
        result += plus_arr[i] * plus_arr[i + 1]
    result += plus_arr[-1]

if len(minus_arr) % 2 == 0:
    for i in range(0, len(minus_arr), 2):
        result += minus_arr[i] * minus_arr[i + 1]
else:
    for i in range(0, len(minus_arr)-1, 2):
        result += minus_arr[i] * minus_arr[i + 1]
    result += minus_arr[-1]

result += sum(one_arr)

print(result)

