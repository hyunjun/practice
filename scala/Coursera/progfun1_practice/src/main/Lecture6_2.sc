//  (1 until n) map (i => (1 until i) map (j => (i, j)))
val n = 7
val xss = (1 until n) map (i => (1 until i) map (j => (i, j)))
//  IndexedSeq; Vector, Range

(xss foldRight Seq[(Int, Int)]())(_ ++ _)
xss.flatten
//  xs flatMap f = (xs map f).flatten

def isPrime(n: Int): Boolean = (2 until n) forall (d => n % d != 0)
xss.flatten filter (pair => isPrime(pair._1 + pair._2))
(1 until n) flatMap (i => (1 until i) map (j => (i, j))) filter (pair => isPrime(pair._1 + pair._2))

//  For-Expression
//  for ( s ) yield e
//  s is a sequence of generators and filters
//    generator p <- e, where p is a pattern and e an expression whose value is a collection
//    filter if f, f is boolean expression
case class Person(name: String, age: Int)
val persons = List(Person("A", 20), Person("B", 21), Person("C", 40))
for ( p <- persons if p.age > 20 ) yield p.name
persons filter (p => p.age > 20) map (p => p.name)

for {
  i <- 1 until n
  j <- 1 until i
  if isPrime(i + j)
} yield (i, j)

def scalarProduct(xs: List[Double], ys: List[Double]): Double =
  (for ( (x, y) <- xs zip ys ) yield x * y).sum