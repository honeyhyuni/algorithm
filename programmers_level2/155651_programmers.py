# https://school.programmers.co.kr/learn/courses/30/lessons/155651
from heapq import heappop, heappush


def solution(book_time):
    heap = []
    book_time = sorted([[int(i.replace(":", "")), int(j.replace(":", ""))] for i, j in book_time],
                       key=lambda x: (x[0], x[1]))
    for start, end in book_time:
        if heap and min(heap) <= start:
            heappop(heap)
        temp = (int(str(end)[-2:]) + 10)
        if temp >= 60:
            end += 50
        else:
            end += 10
        heappush(heap, end)
    return len(heap)


print(solution([["15:00", "17:00"], ["16:40", "18:20"], ["14:20", "15:20"], ["14:10", "19:20"], ["18:20", "21:20"]]))
print(solution([["09:10", "10:10"], ["10:20", "12:20"]]))
print(solution([["10:20", "12:30"], ["10:20", "12:30"], ["10:20", "12:30"]]))
