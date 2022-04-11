# https://programmers.co.kr/learn/courses/30/lessons/42888


def solution(record):
    arr = {}
    answer = []
    for i in range(len(record)):
        record[i] = record[i].split(' ')

    for i in range(len(record)):
        if record[i][0] == "Enter" or record[i][0] == "Change":
            arr[record[i][1]] = record[i][2]

    for i in range(len(record)):
        if record[i][0] == "Enter":
            answer.append((arr[record[i][1]] + "님이 들어왔습니다."))
        elif record[i][0] == "Leave":
            answer.append((arr[record[i][1]] + "님이 나갔습니다."))

    return answer

