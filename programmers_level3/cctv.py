# https://programmers.co.kr/learn/courses/30/lessons/42884
def solution(routes):
    answer = 1
    routes.sort(key= lambda x: x[1])
    camera = routes.pop(0)[1]
    for i, j in routes:
        if camera < i:
            camera = j
            answer += 1
    return answer


print(solution([[-20, -15], [-14, -5], [-18, -13], [-5, -3]]))
