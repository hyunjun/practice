//  Iterable is a base class of Seq, Set, and Map
//  Common base class Seq
//  List; linear
//  Vector; very shallow tree which node is a 32-elements array
val nums = Vector(1, 2, 3, -88)
val people = Vector("Bob", "James", "Peter")

//  +: instead of :: (Cons)
0 +: nums
nums :+ 0

//  Array, and String can be converted into Seq
//  however both are not a subclass of Seq because they come from Java class
val xs = Array(1, 2, 3, 44)
xs map (_ * 2)
val s = "Hello World"
s filter (_.isUpper)

//  Range is a subclass of Seq
val r: Range = 1 until 5
val sr: Range = 1 to 5
1 to 10 by 3
6 to 1 by -2

/*
xs exists p
xs forall p
xs zip ys
xs.unzip
xs.flatMap f
xs.sum
xs.product
xs.max
xs.min
 */
s exists (_.isUpper)
s forall (_.isUpper)

val pairs = List(1, 2, 3) zip s
pairs.unzip

s flatMap (List('.', _))

xs.sum
xs.max
xs.min

(1 to 3) flatMap (x => (1 to 4) map (y => (x, y)))

def scalarProduct(xs: Vector[Double], ys: Vector[Double]): Double =
  (xs zip ys).map(xy => xy._1 * xy._2).sum
scalarProduct(Vector(1, 2, 3), Vector(2, 3, 4))
def scalarProduct2(xs: Vector[Double], ys: Vector[Double]): Double =
  (xs zip ys).map{ case (x, y) => x * y }.sum
scalarProduct2(Vector(1, 2, 3), Vector(2, 3, 4))

def isPrime(n: Int): Boolean = (2 until n) forall (d => n % d != 0)
