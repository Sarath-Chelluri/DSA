# def duplicateinarray(arr):
#     re = []
#     for i in arr:
#         if i not in re:
#             re.append(i)
#         else:
#             print(i)


# duplicateinarray([1, 1, 2, 3, 4, 4])


def fib(n):
    p, q = 0, 1
    while p < n:
        print(p)
        p, q = q, p + q


fib(10)
