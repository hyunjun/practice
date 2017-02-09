# https://www.pramp.com/question/aK6V5GVZ9MSPqvG1vwQp
from collections import Counter
import sys

def different_number(arr):
    if arr is None or 0 == len(arr):
        return None

    arr_len = length(arr)
    if arr_len == sys.maxint + 1:
        return None

    counter = Counter(arr)
    for i in range(max(arr) + 1, -1, -1):
        if counter[i] == 0:
            return i
    return None

print different_number([1, 2, 3])
