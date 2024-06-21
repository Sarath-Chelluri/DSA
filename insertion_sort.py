def insert(alist, index, n):
    # code here
    alist.remove(n)
    alist.insert(index, n)


# Function to sort the list using insertion sort algorithm.
def insertionSort(alist, n):
    for i in range(1, n):
        for j in range(n):
            if alist[i] < alist[j]:
                insert(alist, j, alist[i])
                break


insertionSort([4, 1, 3, 9, 7], 5)
