# https://programmers.co.kr/learn/courses/30/lessons/12953
import math

def solution(arr):
    answer = arr[0]
    for i in arr:
        answer = answer * i // math.gcd(answer, i)
    return answer

print(solution([2, 6, 8, 14]))
print(solution([1, 2, 3]))