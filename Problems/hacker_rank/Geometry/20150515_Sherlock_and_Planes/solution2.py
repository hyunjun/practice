if __name__ == '__main__':
  T = int(raw_input())
  for i in range(T):
    xs, ys, zs = [], [], []
    for j in range(4):
	    x, y, z = (int(n) for n in raw_input().split())
	    xs.append(x)
	    ys.append(y)
	    zs.append(z)
    if 1 == len(set(xs)) or 1 == len(set(ys)) or 1 == len(set(zs)):
	    print 'YES'
    else:
	    print 'NO'
