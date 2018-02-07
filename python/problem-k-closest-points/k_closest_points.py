# https://www.youtube.com/watch?v=eaYX0Ee0Kcg
import math


def k_closest_point(points, k):
  points.sort(key=lambda t: math.sqrt(t[0] * t[0] + t[1] * t[1]))
  return points[:k]


points = [(-2, 4), (0, -2), (-1, 0), (3, 5), (-2, -3), (3, 2)]
print(points)
print(k_closest_point(points, 3))
