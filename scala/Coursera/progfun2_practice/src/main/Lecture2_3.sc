//  Lecture 2-3 Lazy Evaluation
//  by-name evaluation, strict evaluation

//lazy val x = expr
def expr = {
  val x = { print("x"); 1 }
  lazy val y = { print("y"); 2 }
  def z = { print("z"); 3 }
  z + y + x + z + y + x
}
expr

/*
def cons[T](hd: T, tl: => Stream[T]) = new Stream[T] {
  def head = hd
  lazy val tail = tl
}
*/

//  Lecture 2-4 Infinite Streams
def from(n: Int): Stream[Int] = n #:: from(n + 1)

val nats = from(0)  //  all natural numbers
val m4s = nats map (_ * 4)  //  natural numbers multiples 4

(m4s take 100).toList

def sieve(s: Stream[Int]): Stream[Int] =
  s.head #:: sieve(s.tail filter (_ % s.head != 0))

val primes = sieve(from(2))
(primes take 100).toList

def sqrtStream(x: Double): Stream[Double] = {
  def improve(guess: Double) = (guess + x / guess) / 2
  lazy val guesses: Stream[Double] = 1 #:: (guesses map improve)
  guesses
}
sqrtStream(4).take(10).toList
def isGoodEnough(guess: Double, x: Double) =
  math.abs((guess * guess - x) / x) < 0.0001
sqrtStream(4).filter(isGoodEnough(_, 4)).take(10).toList

//  which is faster?
//val xs = from(1) map (_ * N)
//val ys = from(1) filter (_ % N == 0)