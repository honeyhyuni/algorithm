while True:
    n = list(map(int, input()))
    if n[0] == 0:
        break
    elif n == n[::-1]:
        print("yes")
    else:
        print("no")