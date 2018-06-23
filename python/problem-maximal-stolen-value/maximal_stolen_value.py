'''
http://codercareer.blogspot.com/2013/02/no-44-maximal-stolen-values.html

There are n houses built in a line, each of which contains some value in it.
A thief is going to steal the maximal value in these houses, but he cannot steal
in two adjacent houses because the owner of a stolen house will tell his two
neighbors on the left and right side. What is the maximal stolen value?

For example, if there are four houses with values {6, 1, 2, 7}, the maximal
stolen value is 13 when the first and fourth houses are stolen.
'''

def maximal_stolen_value(cur_sum, arr, i):
    if len(arr) <= i:
        return cur_sum

    cur_sum += arr[i]

    cur_max = maximal_stolen_value(cur_sum, arr, i + 2)
    for n in range(i + 3, len(arr)):
        next_max = maximal_stolen_value(cur_sum, arr, n)
        if cur_max < next_max:
            cur_max = next_max

    return cur_max


for d in [[6, 1, 2, 7], [6, 1, 2, 9, 10], [6, 1, 2, 3, 4, 10]]:
    print(d, maximal_stolen_value(0, d, 0))
