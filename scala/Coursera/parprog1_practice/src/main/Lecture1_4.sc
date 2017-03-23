def mySumSegment(a: Array[Int], p: Double, s: Int, t: Int): Int =
  (for ( i <- s until t ) yield Math.pow(a(i), p)).sum.toInt
sumSegment(Array(1, 2, 3, 4, 5), 2.0, 1, 3)

def sumSegment(a: Array[Int], p: Double, s: Int, t: Int): Int = {
  var i = s; var sum: Int = 0
  while ( i < t ) {
    sum = sum + power(a(i), p)
    i = i + 1
  }
  sum
}
def power(x: Int, p: Double): Int = math.exp(p * math.log(math.abs(x))).toInt

def pNorm(a: Array[Int], p: Double): Int =
  power(sumSegment(a, p, 0, a.length), 1 / p)

def pNormTwoPart(a: Array[Int], p: Double): Int = {
  val m = a.length / 2
  val (sum1, sum2) = (sumSegment(a, p, 0, m), sumSegment(a, p, m, a.length))
  power(sum1 + sum2, 1 / p)
}

def pNormTwoPartParallel(a: Array[Int], p: Double): Int = {
  val m = a.length / 2
  val (sum1, sum2) = parallel(sumSegment(a, p, 0, m), sumSegment(a, p, m, a.length))
  power(sum1 + sum2, 1 / p)
}

def pNormRec(a: Array[Int], p: Double): Int =
  power(segmentRec(a, p, 0, a.length), 1 / p)

val threshold = 4
def segmentRec(a: Array[Int], p: Double, s: Int, t: Int) = {
  if ( t - s < threshold )
    sumSegment(a, p, s, t)
  else  {
    val m = s + (t - s) / 2
    val (sum1, sum2) = parallel(segmentRec(a, p, s, m), segmentRec(a, p, m, t))
    sum1 + sum2
  }
}

def parallel[A, B](taskA: => A, taskB: => B): (A, B) = {
  ...
}
//  for parallelism, need to pass unevaluated computations (call by name)
//  (X) def parallel[A, B](taskA: A, taskB: B): (A, B) = { ... }
