//  Lecture 2-2 Streams
//  Streams are simliar to lists, but their tail is evaluated on demand
val xs = Stream.cons(1, Stream.cons(2, Stream.empty))
Stream(1, 2, 3)
(1 to 1000).toStream

def streamRange(lo: Int, hi: Int): Stream[Int] =
  if (lo >= hi) Stream.empty
  else Stream.cons(lo, streamRange(lo + 1, hi))

def listRange(lo: Int, hi: Int): List[Int] =
  if (lo >= hi) Nil
  else lo :: listRange(lo + 1, hi)

1 :: List(2, 3)
1 #:: Stream(2, Stream.empty)

/*
trait Stream[+A] extends Seq[A] {
  def isEmpty: Boolean
  def head: A
  def tail: Stream[A]
}

object Stream {
  def cons[T](hd: T, tl: => Stream[T]) = new Stream[T]  {
    def isEmpty = false
    def head = hd
    def tail = tl
  }
  val empty = new Stream[Nothing] {
    def isEmpty = true
    def head = throw new NoSuchElementException("empty.head")
    def tail = throw new NoSuchElementException("empty.tail")
  }
}

class Stream[+T]  {
  ...
  def filter(p: T => Boolean): Stream[T] =
    if (isEmpty) this
    else if (p(head)) cons(head, tail.filter(p))
    else tail.filter(p)
}
*/
streamRange(1, 10).take(3).toList