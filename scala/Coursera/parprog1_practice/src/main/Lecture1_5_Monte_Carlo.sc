import scala.util.Random

def mcCount(iter: Int): Int = {
  val randomX = new Random
  val randomY = new Random
  var hits = 0
  for ( i <- 0 until iter ) {
    val x = randomX.nextDouble  //  in [0, 1]
    val y = randomY.nextDouble  //  in [0, 1]
    if ( x * x + y * y < 1 )
      hits = hits + 1
  }
  hits
}
def monteCarloPiSeq(iter: Int): Double = 4.0 * mcCount(iter) / iter

def monteCarloPiPar(iter: Int): Double = {
  val ((pi1, pi2), (pi3, pi4)) = parallel(
    parallel(mcCount(iter / 4), mcCount(iter / 4)),
    parallel(mcCount(iter / 4), mcCount(iter - 3 * (iter / 4)))
  )
  4.0 * (pi1 + pi2 + pi3 + pi4) / iter
}

//  More flexible construct for parallel computation
val (v1, v2) = parallel(e1, e2)
val t1 = task(e1)
val t2 = task(e2)
val v1 = t1.join
val v2 = t2.join
//  t = task(e) starts computation e "in the background"
//  t is a task, which performs computation of e
//  current computation proceeds in parallel with t
//  to obtain the result of e, use t.join
//  t.join blocks and waits until the result is computed
//  subsequent t.join calls quickly return the same result

//  minimal interface
def task(c: => A): Task[A]

trait Task[A] {
  def join: A
}
//  task(e).join == e
//  We can omit writing .join if we also define an implicit conversion
implicit def getJoin[T](x: Task[T]): T = x.join

val ((part1, part2), (part3, part4)) =
  parallel(parallel(sumSegment(a, p, 0, mid1),
                    sumSegment(a, p, mid1, mid2)),
           parallel(sumSegment(a, p, mid2, mid3),
                    sumSegment(a, p, mid3, a.length)))
power(part1 + part2 + part3 + part4, 1 / p)
//  the same computation expressed using task
val t1 = task { sumSegment(a, p, 0, mid1) }
val t2 = task { sumSegment(a, p, mid1, mid2) }
val t3 = task { sumSegment(a, p, mid2, mid3) }
val t4 = task { sumSegment(a, p, mid3, a.length) }
power(t1 + t2 + t3 + t4, 1 / p)

//  Can we define parallel using task?
def parallel[A, B](cA: => A, cB: => B): (A, B) = {
  val tB: Task[B] = task { cB }
  val tA: A = cA
  (tA, tB.join) //  tA is a value, tB a task
}

def parallelWrong[A, B](cA: => A, cB: => B): (A, B) = {
  val tB: B = (task { cB }).join
  val tA: A = cA
  (tA, tB)
}
//  cB must complete before the computation of cA starts
