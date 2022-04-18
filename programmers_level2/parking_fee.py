# https://programmers.co.kr/learn/courses/30/lessons/92341
import math
from heapq import heappop, heappush


def solution(fees, records):
    answer = []
    heap = []
    dic = {}
    rate = {}
    for i in records:
        i = i.split()
        heappush(heap, [i[1], i[0], i[2]])
        dic[i[1]] = -1
        rate[i[1]] = 0

    last = 23 * 60 + 59
    while heap:
        x, y, z = heappop(heap)
        if z == "IN":
            dic[x] = (60 * int(y[:2])) + int(y[3:])
        else:
            temp = (60 * int(y[:2])) + int(y[3:]) - dic[x]
            dic[x] = -1
            rate[x] += temp

    for i, j in dic.items():
        if j == -1:
            continue
        else:
            rate[i] += last - j
    heap = []
    for i, j in rate.items():
        if j <= fees[0]:
            heappush(heap, [i, fees[1]])
        else:
            temp = fees[1] + (math.ceil((j - fees[0]) / fees[2])) * fees[3]
            heappush(heap, [i, temp])
    while heap:
        x, y = heappop(heap)
        answer.append(y)
    return answer


print(solution([180, 5000, 10, 600],
               ["05:34 5961 IN", "06:00 0000 IN", "06:34 0000 OUT", "07:59 5961 OUT", "07:59 0148 IN", "18:59 0000 IN",
                "19:09 0148 OUT", "22:59 5961 IN", "23:00 5961 OUT"]))
print(solution([120, 0, 60, 591], ["16:00 3961 IN","16:00 0202 IN","18:00 3961 OUT","18:00 0202 OUT","23:58 3961 IN"]))
print(solution([1, 461, 1, 10], ["00:00 1234 IN"]))
