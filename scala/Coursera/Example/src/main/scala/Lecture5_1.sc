/*def removeAt[T](n: Int, xs: List[T]): List[T] = xs match {
  case List() => xs
  case _ => ((for (i <- 0 to n - 1) yield xs(i)).toList) ++ ((for (i <- n + 1 until xs.size) yield xs(i)).toList)
}*/

def removeAt[T](n: Int, xs: List[T]): List[T] =
  (xs take n) ::: (xs drop n + 1)

//  Lecture 5-2
def msort(xs: List[Int]): List[Int] = {
  val n = xs.length / 2
  if ( n == 0 ) xs
  else  {
    def merge(xs: List[Int], ys: List[Int]) = xs match {
      case Nil => ys
      case x :: xs1 => ys match {
        case Nil => xs
        case y :: ys1 => if ( x < y ) x :: merge(xs1, ys)
                         else y :: merge(xs, ys1)
      }
    }
    val (fst, snd) = xs splitAt n
    merge(msort(fst), msort(snd))
  }
}

def merge(xs: List[Int], ys: List[Int]): List[Int] = (xs, ys) match {
  case (Nil, ys) => ys
  case (xs, Nil) => xs
  case (x :: xs1, y :: ys1) =>
    if ( x < y ) x :: merge(xs1, ys)
    else y :: merge(xs, ys1)
}