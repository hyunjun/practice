/*
abstract class Boolean  {
  def ifThenElse[T](t: => T, e: => T): T

  def && (x: => Boolean): Boolean = ifThenElse(x, false)
  def || (x: => Boolean): Boolean = ifThenElse(true, x)
  def unary_! : Boolean           = ifThenElse(false, true)

  def == (x: Boolean): Boolean    = ifThenElse(x, x.unary_!)
  def != (x: Boolean): Boolean    = ifThenElse(x.unary_!, x)
}

object true extends Boolean {
  def ifThenElse[T](t: => T, e: => T) = t
}

object false extends Boolean {
  def ifThenElse[T](t: => T, e: => T) = e
}

class Int {
  def + (that: Double): Double
  def + (that: Float): Float
  def + (that: Long): Long
  def + (that: Int): Int

  def << (cnt: Int): Int
  def & (that: Long): Long
  def & (that: Int): Int
}
 */

//  Peano numbers
abstract class Nat  {
  def isZero: Boolean
  def predecessor: Nat
  def successor: Nat
  def + (that: Nat): Nat
  def - (that: Nat): Nat
}

object Zero extends Nat {
  def isZero = true
  def predecessor = throw new Error("0.predecessor")
  def successor = new Succ(this)
  def + (that: Nat) = that
  def - (that: Nat) = if ( that.isZero ) this else throw new Error("negative number")
}

class Succ(n: Nat) extends Nat  {
  def isZero = false
  def predecessor = n
  def successor = new Succ(this)
  def + (that: Nat): Nat = new Succ(n + that)
  def - (that: Nat): Nat = if ( that.isZero ) this else n - that.predecessor //  n = this - 1, that.predecessor = that - 1
}

//  Lecture 4-2
(x: Int) => x * x
/*  is expnaded to
  { class AnonFun extends Function1[Int, Int] {
    def apply(x: Int) = x * x
    }
    new AnnoFun
  }

  or

  new Function1[Int, Int] {
    def apply(x: Int) = x * x
  }
 */
val f = (x: Int) => x * x
f(7)
val f2 = new Function1[Int, Int]  {
  def apply(x: Int) = x * x
}
f2.apply(7)
def f3(x: Int): Boolean = if ( x % 2 == 0 ) true else false
(x: Int) => f3(x)
new Function1[Int, Boolean] { //  eta expansion
  def apply(x: Int) = f3(x)
}

