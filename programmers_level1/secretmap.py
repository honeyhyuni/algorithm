# https://programmers.co.kr/learn/courses/30/lessons/17681
def solution(n, arr1, arr2):
    arr = []
    for i in range(n):
        ct = format(arr1[i], 'b')
        ct2 = format(arr2[i], 'b')
        st = ""
        for _ in range(n - len(ct)):
            ct = "0" + ct
        for _ in range(n - len(ct2)):
            ct2 = "0" + ct2
        for _ in range(n):
            if ct[_] == "1" or ct2[_] == "1":
                st += "#"
            else:
                st += " "
        arr.append(st)
    return arr

print(solution(5, [9, 20, 28, 18, 11], [30, 1, 21, 17, 28]))