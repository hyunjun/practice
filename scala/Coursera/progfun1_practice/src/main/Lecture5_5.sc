def recursiveSum(xs: List[Int]): Int = xs match {
  case Nil => 0
  case y :: ys => y + recursiveSum(ys)
}

//  List(x1, ..., xn) reduceLeft op = (... (x1 op x2) op ...) op xn
//def sum(xs: List[Int]): Int = (0 :: xs) reduceLeft ((x, y) => x + y)
//def product(xs: List[Int]) = (1 :: xs) reduceLeft ((x, y) => x * y)
//  every _ represents a new parameter, going from left to right
//def sum(xs: List[Int]): Int = (0 :: xs) reduceLeft (_ + _)
//def product(xs: List[Int]) = (1 :: xs) reduceLeft (_ * _)

//  (List(x1, ..., xn) foldLeft z)(op) = (...(z op x1) op ...) op xn
//  z; accumulator
//  draw left skewed tree to understand this visually
def sum(xs: List[Int]) = (xs foldLeft 0)(_ + _)
def product(xs: List[Int]) = (xs foldLeft 1)(_ * _)

//  List(x1, ..., x{n-1}, xn) reduceRight op = x1 op ( ... ( x{n-1} op xn) ...)
//  (List(x1, ..., xn) foldRight acc)(op) = x1 op ( ... (xn op acc) ...)
//  draw right skewed tree to understand this visually
val xs = List('a', 'b', 'c')
val ys = List(1, 2, 3)
(xs foldRight ys)(_ :: _)
//  (xs foldLeft ys)(_ :: _)  //  not working why?

def mapFun[T, U](xs: List[T], f: T => U): List[U] =
  (xs foldRight List[U]())((x: T, xs1: List[U]) => f(x) :: xs1)
mapFun(ys, (x: Int) => x * 1.5)

def lengthFun[T](xs: List[T]): Int =
  (xs foldRight 0)((x: T, acc: Int) => acc + 1)
lengthFun(xs)