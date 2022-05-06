# https://www.acmicpc.net/problem/1644
n = int(input())
answer = []
for i in range(2, n+1):
    for j in range(2, int(i ** 0.5)+1):
        if i % j == 0:
            break
    else:
        answer.append(i)
left, right = 0, 1
result = 0
while right <= len(answer):
    sum_ = sum(answer[left: right])
    if sum_ == n:
        result += 1
    if sum_ < n:
        right += 1
    if sum_ >= n:
        left += 1
print(result)