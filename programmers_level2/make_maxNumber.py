# https://programmers.co.kr/learn/courses/30/lessons/42883
def solution(number, k):
    answer = []
    for i in number:
        if not answer:
            answer.append(i)
            continue
        if k > 0:
            while answer[-1] < i:
                answer.pop()
                k -= 1
                if k == 0 or not answer:
                    break
        answer.append(i)
    return "".join(answer[:len(answer)-k])

print(solution("1924", 2))
print(solution("1231234", 3))
print(solution("4177252841", 4))