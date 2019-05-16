#   https://aonecode.com/amazon-online-assessment-questions Q1


def longest_movie_times(movie_duration, d):
    if movie_duration is None or 0 == len(movie_duration):
        return 0
    d -= 30
    movie_duration.sort()
    l, r = 0, len(movie_duration) - 1
    max_sum, max_sum_pair = 0, [0, 0]
    while l < r:
        cur_sum = movie_duration[l] + movie_duration[r]
        if cur_sum == d:
            return [movie_duration[l], movie_duration[r]]
        if max_sum < cur_sum <= d:
            max_sum, max_sum_pair = cur_sum, [movie_duration[l], movie_duration[r]]
        if cur_sum < d:
            l += 1
        else:
            r -= 1
    return max_sum_pair


data = [([90, 85, 75, 60, 120, 150, 125], 250, [90, 125]),
        ]
for movie_duration, d, expected in data:
    real = longest_movie_times(movie_duration, d)
    print('{}, {}, expected {}, real {}, result {}'.format(movie_duration, d, expected, real, expected == real))
