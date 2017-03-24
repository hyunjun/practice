//  Asymptotic analysis of sequential running time
//  inserting an integer into a sorted linear list O(n)
//  inserting an integer into a balanced binary tree O(log n)

def sumSegment(a: Array[Int], p: Double, s: Int, t: Int): Int = {
  var i = s; var sum: Int = 0
  while ( i < t ) {
    sum = sum + power(a(i), p)
    i = i + 1
  }
  sum
}
def power(x: Int, p: Double): Int = math.exp(p * math.log(math.abs(x))).toInt
//  W(s, t) = O(t - s), a function of the form c1(t - s) + c2

val threshold = 4
def segmentRec(a: Array[Int], p: Double, s: Int, t: Int): Int = {
  if ( t - s < threshold )
    sumSegment(a, p, s, t)
  else  {
    val m = s + (t - s) / 2
    val (sum1, sum2) = (segmentRec(a, p, s, m), segmentRec(a, p, m, t))
    sum1 + sum2
  }
}
//  W(s, t) =
//    c1(t - s) + c2 if t - s < threshold
//    W(s, m) + W(m, t) + c3 otherwise, for m = round of (s + t) / 2
//  O(t - s)

/*
val threshold = 4
def segmentRec(a: Array[Int], p: Double, s: Int, t: Int): Int = {
  if ( t - s < threshold )
    sumSegment(a, p, s, t)
  else  {
    val m = s + (t - s) / 2
    val (sum1, sum2) = parallel(segmentRec(a, p, s, m), segmentRec(a, p, m, t))
    sum1 + sum2
  }
}
//  D(s, t) =
//    c1(t - s) + c2 if t - s < threshold
//    max(D(s, m) + D(m, t)) + c3 otherwise, for m = round of (s + t) / 2
//  O(log(t - s))
*/

/*
Work W(e): number of steps e would take if there was no parallelism
  this is simply the sequential execution time
  treat all parallel(e1, e2) as (e1, e2)
  parallel(e1, e2) = W(e1) + W(e2) + c2

Depth D(e): number of steps if we had unbounded parallelism
  we take maximum of running time for arguments of parallel
  parallel(e1, e2) = max(D(e1), D(e2)) + c1

W(f(e1, ..., en)) = W(e1) + ... + W(en) + W(f)(v1, ... vn)
D(f(e1, ..., en)) = D(e1) + ... + D(en) + D(f)(v1, ... vn)
vi = value of ei
if f is primitive operation on integers, then W(f) and D(f) are constant functions, regardless of vi

D(e) + W(e) / P
  Even if P goes infinite, still have non-zero complexity give by D(e)
 */

/*
part1 fraction f of the computation time
part2 1 - f and we can speed it up
1 / (f + (1-f) / P)
P = 100, f = 0.4 > we obtain 2.46
Even if we speed the second part infinitely, we can obtain 2.5
 */