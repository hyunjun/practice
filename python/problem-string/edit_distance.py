
def edit_distance(s1, s2):
    long = s1
    short = s2
    if len(s1) < len(s2):
        long = s2
        short = s1

    for l in range(len(short) - 1):
        if short[l:l+1] != long[l:l+1]:
            break
    print(l)
    r = -1
    while -len(short) < r:
        if short[r-1:r] != long[r-1:r]:
            break
        r -= 1
    print(r)
    print(short[l:len(short)+r], long[l:len(long)+r])

    return edit_distance_r(short[l:len(short)+r], long[l:len(long)+r])

def edit_distance_r(short, long):
    print('edit_distance_r', short, long)

    if short[:1] == long[:1]:
        return edit_distance_r(short[1:], long[1:])

    if len(short) == 1:
        if short[:1] in long:
            return len(long) - 1
        return len(long)
    return min(edit_distance_r(short[1:], long), edit_distance_r(short, long[1:])) + 1


if __name__ == '__main__':
    print(edit_distance('Saturday', 'Sunday'))
