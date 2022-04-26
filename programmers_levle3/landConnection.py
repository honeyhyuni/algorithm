# https://programmers.co.kr/learn/courses/30/lessons/42861#
def solution(n, costs):
    # 비용 오름차순, 크루스칼
    costs.sort(key= lambda x :x[2])
    land = set()
    land.add(costs[0][0])
    answer = 0
    while len(land) < n:
        for i in costs:
            if i[0] in land and i[1] in land:
                continue
            elif i[0] in land or i[1] in land:
                answer += i[2]
                land.update((i[0], i[1]))
                break
    return answer


print(solution(4, [[0 ,1 ,1] ,[0 ,2 ,2] ,[1 ,2 ,5] ,[1 ,3 ,1] ,[2 ,3 ,8]]))
print(solution(6, [[0, 1, 5], [0, 3, 2], [0, 4, 3], [1, 4, 1], [3, 4, 10], [1, 2, 2], [2, 5, 3], [4, 5, 4]]))
print(solution(5, [[0, 1, 1], [3, 4, 1], [1, 2, 2], [2, 3, 4]]))
print(solution(5, [[0, 1, 5], [1, 2, 3], [2, 3, 3], [3, 1, 2], [3, 0, 4], [2, 4, 6], [4, 0, 7]]))
