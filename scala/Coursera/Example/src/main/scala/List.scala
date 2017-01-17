import java.util.NoSuchElementException

/**
  * Created by jun on 2017. 1. 9..
  * Lecture 3-3
  */
trait List[T] {
  def isEmpty: Boolean
  def head: T
  def tail: List[T]
}

class Cons[T](val head: T, val tail: List[T]) extends List[T] {
  def isEmpty = false
}

class Nil[T] extends List[T]  {
  def isEmpty = true
  def head: Nothing = throw new NoSuchElementException("Nil.head")
  def tail: Nothing = throw new NoSuchElementException("Nil.tail")
}

//  Lecture 4-2
object List {
  //  List(1, 2)
  def apply[T](x1: T, x2: T): List[T] = new Cons(x1, new Cons(x2, new Nil))
  def apply[T](x: T): List[T] = new Cons(x, new Nil)
  def apply[T](): List[T] = new Nil
}
