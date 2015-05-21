import math

if __name__ == '__main__':
  T = int(raw_input())
  for i in range(T):
    inps = [int(n) for n in raw_input().split()]
    res, D, P = [], inps[0], inps[1]
    if 0 <= D:
      discriminant = D**2 + 4*P
      if 0 <= discriminant:
	      x = math.sqrt(discriminant)
	      if x == 0 or x == int(x):
	        As = [(D + x) / 2, (D - x) / 2, (-D + x) / 2, (-D - x) / 2]
	        Bs = [(-D + x) / 2, (-D - x) / 2, (D + x) / 2, (D - x) / 2]
	        for i in range(len(As)):
	          if abs(As[i] - Bs[i]) == D and As[i] * Bs[i] == P:
	            res.append((As[i], Bs[i]))
    print len(set(res))
