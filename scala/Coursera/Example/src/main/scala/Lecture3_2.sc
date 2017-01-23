import example.Example

Example

trait Planar  {
  def height: Int
  def width: Int
  def surface = height * width
}
//  inherit from at most one class but arbitrary many traits
//  class Square extends Shape with Planar with Movable ...

def error(msg: String) = throw new Error(msg) //  Nothing means NOT normal end
//error("test")

val x = null  //  subtype only for ref
val y: String = x
//val z: Int = null //error

if ( true ) 1 else false

//  Lecture 3-3
List(1, 2, 3)
List(List(true, false), List(3))

/*
trait IntList
class Cons(val head: Int, val tail: IntList) extends IntList
class Nil extends IntList

trait List[T]
class Cons[T](val head: T, val tail: List[T]) extends List[T]
class Nil[T] extends List[T]
 */


def singleton[T](elem: T) = new Cons[T](elem, new Nil[T])
singleton[Int](1)
singleton[Boolean](true)
/*
def nth[T](n: Int, xs: List[T]): T = {
  def _nth(acc: Int, i: Int, ts: List[T]): T =
    if ( acc == i ) {
      ts.head
    } else {
      _nth(acc + 1, i, ts.tail)
    }
  _nth(0, n, xs)
}
*/
def nth[T](n: Int, xs: List[T]): T =
  if ( xs.isEmpty ) throw new IndexOutOfBoundsException
  else if ( 0 == n ) xs.head
  else nth(n - 1, xs.tail)
val testList = new Cons(0, new Cons(1, new Cons(2, new Nil)))
testList.head
nth(2, testList)
nth(-1, testList)

//  Lecture 4-4
trait List[+T] {
  def isEmpty: Boolean
  def head: T
  def tail: List[T]
  //def prepend(elem: T): List[T] = new Cons(elem, this)
  def prepend[U >: T](elem: U): List[U] = new Cons(elem, this)
}
class Cons[T](val head: T, val tail: List[T]) extends List[T] {
  def isEmpty = false
}
//class Nil[T] extends List[T] {
object Nil extends List[Nothing] {
  def isEmpty: Boolean = false
  def head: Nothing = throw new NoSuchElementException("Nil.head")
  def tail: Nothing = throw new NoSuchElementException("Nil.tail")
}
object test {
  val x: List[String] = Nil //  error unless trait List[+T]? DOES NOT WORK
  def f(xs: List[NonEmpty], x: Empty) = xs prepend x
}