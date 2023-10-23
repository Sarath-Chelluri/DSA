arr = list(map(int, input().split()))


def inversion_pain_count(arr, n):
    count = 0
    for i in range(n):
        for j in range(i, n):
            if arr[i] > arr[j]:
                count += 1
    return count


print(inversion_pain_count(arr, len(arr)))
