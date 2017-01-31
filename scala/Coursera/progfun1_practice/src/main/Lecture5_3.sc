//  msort only for List[Int] from lecture 5-2
def msortInt(xs: List[Int]): List[Int] = {
  val n = xs.length / 2
  if ( n == 0 ) xs
  else  {
    def merge(xs: List[Int], ys: List[Int]): List[Int] = (xs, ys) match {
      case (Nil, ys) => ys
      case (xs, Nil) => xs
      case (x :: xs1, y :: ys1) =>
        if ( x < y ) x :: merge(xs1, ys)
        else y :: merge(xs, ys1)
    }

    val (fst, snd) = xs splitAt n
    merge(msortInt(fst), msortInt(snd))
  }
}

val nums = List(2, -4, 5, 7, 1)
msortInt(nums)

def msort[T](xs: List[T])(lt: (T, T) => Boolean): List[T] = {
  val n = xs.length / 2
  if ( n == 0 ) xs
  else  {
    def merge(xs: List[T], ys: List[T]): List[T] = (xs, ys) match {
      case (Nil, ys) => ys
      case (xs, Nil) => xs
      case (x :: xs1, y :: ys1) =>
        if ( lt(x, y) ) x :: merge(xs1, ys)
        else y :: merge(xs, ys1)
    }

    val (fst, snd) = xs splitAt n
    merge(msort(fst)(lt), msort(snd)(lt))
  }
}

msort(nums)((x, y) => x < y)
val fruits = List("apple", "pineapple", "orange", "banana")
msort(fruits)((x: String, y: String) => x.compareTo(y) < 0) //  compareTo is a java function

//  scala.math.Ordering[T]
def msort2[T](xs: List[T])(ord: Ordering[T]): List[T] = {
  val n = xs.length / 2
  if ( n == 0 ) xs
  else  {
    def merge(xs: List[T], ys: List[T]): List[T] = (xs, ys) match {
      case (Nil, ys) => ys
      case (xs, Nil) => xs
      case (x :: xs1, y :: ys1) =>
        if ( ord.lt(x, y) ) x :: merge(xs1, ys)
        else y :: merge(xs, ys1)
    }

    val (fst, snd) = xs splitAt n
    merge(msort2(fst)(ord), msort2(snd)(ord))
  }
}
msort2(nums)(Ordering.Int)
msort2(fruits)(Ordering.String)

//  implicit
def msort3[T](xs: List[T])(implicit ord: Ordering[T]): List[T] = {
  val n = xs.length / 2
  if ( n == 0 ) xs
  else  {
    def merge(xs: List[T], ys: List[T]): List[T] = (xs, ys) match {
      case (Nil, ys) => ys
      case (xs, Nil) => xs
      case (x :: xs1, y :: ys1) =>
        if ( ord.lt(x, y) ) x :: merge(xs1, ys)
        else y :: merge(xs, ys1)
    }

    val (fst, snd) = xs splitAt n
    merge(msort3(fst), msort3(snd))
  }
}
msort3(nums)
msort3(fruits)
