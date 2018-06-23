l = [1, 23, 12, 9, 30, 2, 50]


def heapify(arr, n, i):
    largest = i
    l, r = 2 * i + 1, 2 * i + 2
    if l < n and arr[i] < arr[l]:
        largest = l
    if r < n and arr[largest] < arr[r]:
        largest = r
    if largest != i:
        arr[i], arr[largest] = arr[largest], arr[i]
        heapify(arr, n, largest)


def heapsort(arr):
    n = len(arr)

    for i in range(n - 1, -1, -1):
        heapify(arr, n, i)


def kth_largest(arr, k):
    n = len(arr)

    for i in range(k):
        arr[0], arr[len(arr) - 1] = arr[len(arr) - 1], arr[0]
        print(arr.pop())
        heapify(arr, len(arr), 0)


print(l)
heapsort(l)
print(l)
kth_largest(l, 3)
