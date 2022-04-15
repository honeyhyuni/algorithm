# https://programmers.co.kr/learn/courses/30/lessons/17686
def solution(files):
    answer = []
    result = []
    for i in files:
        head, number, tail = "", "", ""
        bol = False
        for j in range(len(i)):
            if i[j].isdigit():
                number += i[j]
                bol = True
            elif not bol:
                head += i[j]
            else:
                tail += i[j:]
                break
        answer.append((head,number,tail))
    answer.sort(key=lambda x: (x[0].lower(), int(x[1])))
    for i in answer:
        i = "".join(i)
        result.append(i)
    return result

print(solution(["img12.png", "img10.png", "img02.png", "img1.png", "IMG01.GIF", "img2.JPG"]))
print(solution(["F-5 Freedom Fighter", "B-50 Superfortress", "A-10 Thunderbolt II", "F-14 Tomcat"]))