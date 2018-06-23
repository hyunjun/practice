#   continuous sequence of array that sums up to exactly T
#   array, T
l1, s1 = [23, 5, 4, 7, 2, 11], 20
l2, s2 = [1, 3, 5, 23, 2], 8
l3, s3 = [1, 3, 5, 23, 2], 7


def foo(A, T):
    sum_list = []
    for i, item in enumerate(A):
        if T < item:
            sum_list.append(0)
        else:
            if i == 0:
                sum_list.append(item)
            else:
                sum_list.append(item + sum_list[i - 1])
    r = len(A) - 1
    while sum_list[r] < T:
        r -= 1
    l = r - 1
    while 0 <= l and sum_list[r] - sum_list[l] <= T:
        if sum_list[r] - sum_list[l] == T:
            print('result {}\t{} ~ {} == {}'.format(A, A[l], A[r], T))
            break
        l -= 1

foo(l1, s1)
print()
foo(l2, s2)
print()
foo(l3, s3)
