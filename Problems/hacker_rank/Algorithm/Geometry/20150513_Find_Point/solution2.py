if __name__ == '__main__':
  T = int(raw_input())
  for i in range(T):
    inps = [int(n) for n in raw_input().split()]
    Px, Py, Qx, Qy = inps[0], inps[1], inps[2], inps[3]
    # print Px, Py, Qx, Qy
    print Qx + (Qx - Px), Qy + (Qy - Py)
