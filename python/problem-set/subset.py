#   https://www.youtube.com/watch?v=eRvn5g9jOh0&list=PLVNY1HnUlO24RlncfRjfoZHnD0YWVsvhq&index=22
from copy import deepcopy


def subset(arr):
    if 0 == len(arr):
        return [[]]
    else:
        last = arr[-1]
        arr.remove(last)
        prev = subset(arr)
        cur = deepcopy(prev)
        [i.append(last) for i in cur]
        prev.extend(cur)
        return prev


for d in [ [], [0], [0, 1], [0, 1, 2] ]:
    print('{}\t{}'.format(d, subset(d)))
