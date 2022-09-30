# https://school.programmers.co.kr/learn/courses/30/lessons/120863
def solution(polynomial):
    x, n_x = 0, 0
    polynomial = polynomial.split(" + ")
    for i in polynomial:
        if i.isnumeric():
            n_x += int(i)
        else:
            if len(i) == 1:
                x += 1
            else:
                x += int(i[:-1])
    x, n_x = str(x), str(n_x)
    if x == "0": return n_x
    if x == "1": x = ""
    if n_x == "0": return x + "x"
    return x + "x + " + n_x


print(solution("3x + 7 + x"))
print(solution("x + x + x"))
print(solution("3 + 3"))
print(solution("0 + 0"))
print(solution("123x + 7 + 123x + 123 + 1232134x + 123 + 123 + 123 + 123 + 123 + 123 + 123"))
print(solution("x + 0"))
