def count_time(num, chefs):
    min_A, min_B, c = 0, 0, 0
    for i, j in chefs.items():
        if i == "A":
            min_A = min(j)
            print(i, j, min_A)
        if i == "B":
            min_B = min(j)
            print(i, j, min_B)
        if i == "C":
            c = min(j)
            print(i, j, c)
    if min_A + min_B > c:
        return c
    else:
        return min_A + min_B


n = int(input())
chef = {"A": [], "B": [], "C": []}
for i in range(n):
    c, t = input().split(" ")
    chef[c].append(int(t))

print(count_time(n, chef))
