//  Using sum. array of norm
//  reduce(map(a, power(abs(_), p)), _ + _)
List(1, 3, 8).map(t => t * t).reduce(_ + _)


/*  associative but not commutative
    reduce still gives the same result because they are associative
 */
//  concatenation (append) of lists
//  concatenation of Strings
//  matrix multiplication AB
//  composition of relations
//  composition of functions

/*  Many operations are commutative but not associative
    f(x, y) = x * x + y * y

    f(x, y) == f(y, x)
    f(f(x, y), z) != f(x, f(y, z))
 */

//  associativity is not preserved by mapping

val e = 1e-200
val x = 1e200
val mx = -x

//  floating point addition is commutative but not associative
val a = (x + mx) + e
val b = x + (mx + e)  //  mx + e is not calculated precisely
a == b

//  floating point multiplication is commutative but not associative
val c = (e * x) * x
val d = e * (x * x)
c == d

//  commutative operation
//def f(x: A, y: A) = if ( less(y, x) ) g(y, x) else g(x, y)

/////////////////////////////////////////////////
//  Lecture 2-5
/////////////////////////////////////////////////

//  Associative operations on tuples
//  f1: (A1, A1) => A1 and f2: (A2, A2) => A2
//  f: ((A1, A2), (A1, A2)) => (A1, A2) defined by
//  f((x1, x2), (y1, y2)) = (f1(x1, y1), f2(x2, y2)) is also associative
//  This also applied for n-tuples

//  rational multiplication

//  average
//val sum = reduce(collection, _+_)
//val length = reduce(map(collection, (x: Int) => 1), _ + _)
//sum / length
//  This includes two reductions. Is there a solution using a single reduce?
//  f((sum1, len1), (sum2, len2)) = (sum1 + sum2, len1 + len2)
//val (sum, length) = reduce(map(collection, (x: Int) => (x, 1)), f)

//  associativity through symmetry and commutativity
//  E(x, y, z) = f(f(x, y), z)
//  f(f(x, y), z) = f(f(y, z), x)
//  f(f(x, y), z) = f(f(y, z), x) = f(x, f(y, z))

//  addition of mudular fractions
//  plus((x1, y1), (x2, y2)) = (x1 * y2 + x2 * y1, y1 * y2)
//  associative?
//  my solution
//  plus(plus((x1, y1), (x2, y2)), (x3, y3))
//    plus((x1 * y2 + x2 * y1, y1 * y2), (x3, y3))
//    ((x1 * y2 + x2 * y1) * y3 + x3 * (y1 * y2), (y1 * y2) * y3)
//    (x1 * y2 * y3 + x2 * y1 * y3 + x3 * y1 * y2, y1 * y2 * y3)
//  plus((x1, y1), plus((x2, y2), (x3, y3)))
//    plus((x1, y1), (x2 * y3 + x3 * y2, y2 * y3))
//    (x1 * (y2 * y3) + (x2 * y3 + x3 * y2) * y1, y1 * (y2 * y3))
//    (x1 * y2 * y3 + y1 * x2 * y3 + x3 * y2 * y1, y1 * y2 * y3)
//  lecturer's solution
//  plus is commutative
//  E((x1, y1), (x2, y2), (x3, y3)) == ...
//  E((x2, y2), (x3, y3), (x1, y1)) == ...

//  relativistic velocity addition
//  f(u, v) = (u + v) / (1 + uv)
//  u, v are in the interval (-1, 1)
//  show that (1 - u)(1 - v) > 0 and thus (u + v)/(1 + uv) < 1
//  my solution
//    -1 < u < 1, so -1 < -u < 1, so 0 < 1 - u < 2
//    0 < (1 - u)(1 - v) < 4
//    0 < 1 - u - v + uv < 4
//    0 < 1 + uv - (u + v)
//    (u + v) < 1 + uv
//    (u + v) / (1 + uv) < 1
//  f is commutative; f(u, v) = f(v, u)
//  E(u, v, w) = f(f(u, v), w) == E(v, w, u)
def f(u: Double, v: Double): Double = (u + v) / (1.0 + u * v)
def err(lst: List[Double]): Double =
  lst.reduceLeft(f) - lst.reduceRight(f)
def testAssoc: Double = {
  val r = new scala.util.Random
  val lst = List.fill(400)(r.nextDouble * 0.002)
  err(lst)
}
testAssoc