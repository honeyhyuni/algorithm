# https://programmers.co.kr/learn/courses/30/lessons/42628
from heapq import heappop, heappush
def solution(operations):
    heap = []
    for i in operations:
        i = i.split()
        if i[0] == "I":
            heappush(heap, int(i[1]))
        else:
            if heap:
                if i[1] == "-1":
                    heappop(heap)
                else:
                    heap.pop(heap.index(max(heap)))
    if not heap:
        return [0, 0]
    return [max(heap), min(heap)]


print(solution(["I 16","D 1"]))
print(solution(["I 7","I 5","I -5","D -1"]))