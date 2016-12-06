#   https://www.youtube.com/watch?v=sl_P4qxPfwM&index=23&list=PLVNY1HnUlO24RlncfRjfoZHnD0YWVsvhq
def perm(prev, arr):
    if len(arr) <= 1:
        print prev, arr
    else:
        for i in range(len(arr)):
            arr[i], arr[0] = arr[0], arr[i]
            prev.append(arr[0])
            arr.remove(arr[0])
            perm(prev, arr)
            arr.insert(0, prev.pop())
            arr[i], arr[0] = arr[0], arr[i]

perm([], [])
perm([], [0])
perm([], [0, 1])
perm([], [0, 1, 2])
