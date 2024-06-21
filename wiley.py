def max_separation(N, K, arr):
    b = [0] * (N + 1)
    c = []
    cnt = 0

    b = []

    for i in range(1, N + 1):
        if arr[i - 1] % 2 == 1:
            b[i] = 1
        else:
            b[i] = -1

    for i in range(1, N + 1):
        b[i] += b[i - 1]

    for i in range(1, N):
        if b[i] == 0:
            c.append(abs(arr[i] - arr[i - 1]))

    c.sort()

    pt = 0
    cost = 0

    while pt < len(c) and cost + c[pt] <= K:
        cost += c[pt]
        pt += 1

    return pt
