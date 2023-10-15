def find_distant(arr, n):
    l = n - len(set(arr))
    return len(set(arr)) - l


print(find_distant([5, 8, 5, 7, 8, 10], 6))
[1,2,3,4,5,6,7]
