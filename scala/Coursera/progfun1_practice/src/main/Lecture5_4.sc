def scaleList(xs: List[Double], factor: Double): List[Double] = xs match {
  case Nil => xs
  case y :: ys => y * factor :: scaleList(ys, factor)
}
def scaleList2(xs: List[Double], factor: Double) =
  xs map (x => x * factor)

def squareList(xs: List[Int]): List[Int] = xs match {
  case Nil => xs
  case y :: ys => y * y :: squareList(ys)
}
def squareList2(xs: List[Int]): List[Int] =
  xs map (x => x * x)

def posElems(xs: List[Int]): List[Int] = xs match {
  case Nil => xs
  case y :: ys => if ( y > 0 ) y :: posElems(ys) else posElems(ys)
}
def posElems2(xs: List[Int]): List[Int] =
  xs filter (_ > 0)

val nums = List(2, -4, 5, 7, 1)
val fruits = List("apple", "pineapple", "orange", "banana")

nums filter (_ > 0)
nums filterNot (_ > 0)
nums partition (_ > 0)
nums takeWhile (_ > 0)
nums dropWhile (_ > 0)
nums span (_ > 0)

def pack[T](xs: List[T]): List[List[T]] = xs match {
  case Nil => Nil
  case x :: xs1 =>
    //(x :: xs1 takeWhile (_ == x) ) :: pack(xs1 dropWhile (_ == x))
    val (first, rest) = xs span (y => y == x)
    first :: pack(rest)
}
val data = List("a", "a", "a", "b", "c", "c", "a")
pack(data)

def encode[T](xs: List[T]): List[(T, Int)] = xs match {
  case Nil => Nil
  case x :: xs1 =>
    val (first, rest) = xs span (_ == x)
    (first.head, first.length) :: encode(rest)
}
//  pack(xs) map (ys => (ys.head, ys.length))
encode(data)