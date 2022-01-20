n = int(input())
a = []
for _ in range(n):
    a = list(input())
    sum = 0
    k = 1
    for q in range(len(a)):
        if a[q] == "O":
            sum += k
            k += 1
        else:
            k = 1
    print(sum)

