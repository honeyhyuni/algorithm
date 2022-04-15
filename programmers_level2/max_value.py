# https://programmers.co.kr/learn/courses/30/lessons/42746
def solution(numbers):
    numbers = list(map(str, numbers))
    numbers.sort(key=lambda x: x*3, reverse=True)
    return str(int(''.join(numbers)))


print(solution([6, 10, 2]))
print(solution([3, 30, 34, 5, 9]))
