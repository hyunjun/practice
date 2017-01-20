abstract class IntSet {
  def incl(x: Int): IntSet
  def contains(x: Int): Boolean

  def union(other: IntSet): IntSet
}

//class Empty extends IntSet  {
object Empty extends IntSet  {  //  singleton object == value
  def contains(x: Int): Boolean = false
  //def incl(x: Int): IntSet = new NonEmpty(x, new Empty, new Empty)
  def incl(x: Int): IntSet = new NonEmpty(x, Empty, Empty)
  override def toString = "."

  def union(other: IntSet): IntSet = other
}

class NonEmpty(elem: Int, left: IntSet, right: IntSet) extends IntSet {
  def contains(x: Int): Boolean =
    if ( x < elem ) left contains x
    else if ( x > elem ) right contains x
    else true

  def incl(x: Int): IntSet =
    if ( x < elem ) new NonEmpty(elem, left incl x, right)
    else if ( x > elem ) new NonEmpty(elem, left, right incl x)
    else this

  override def toString = "{" + left + elem + right + "}"

  def union(other: IntSet): IntSet =
    ((left union right) union other) incl elem
}

//  persistent data structures

//val t1 = new NonEmpty(3, new Empty, new Empty)
val t1 = new NonEmpty(3, Empty, Empty)
val t2 = t1 incl 4

abstract class Base {
  def foo = 1
  def bar: Int
}
class Sub extends Base  {
  override def foo = 2
  def bar = 3
}

//  dynamic binding
Empty contains 1
(new NonEmpty(7, Empty, Empty)) contains 7

//  Lecture 4-3
//  S <: T  S is a subtype of T
def assertAllPos[S <: IntSet](r: S): S
//  [S >: NonEmpty <: IntSet] //  mix a lower bound with an upper bound

//  NonEmpty <: IntSet
//  List[NonEmpty] <: List[IntSet]   // covariant

//  Array Typing Problem (Java)
/*
NonEmpty[] a = new NonEmpty[]{new NonEmpty(1, Empty, Empty)}
IntSet[] b = a
b[0] = Empty
NonEmpty s = a[0]
 */
//  Liskov
//  Let q(x) be a property provable about objects x of type
//  Then q(y) should be provable for objects y of type A where A <: B
/*
val a: Array[NonEmpty] = Array(new NonEmpty(1, Empty, Empty))
val b: Array[IntSet] = a  //  error, because scala array is not covariant
b(0) = Empty
val s: NonEmpty = a(0)
*/

//  Lecture 4-4
/*  immutable types can be covariant, if some condition met
A <: B
c[A] <: C[B]  covariant
c[A] >: C[B]  contravariant
neither C[A] nor C[B] is a subtype of the other nonvariant

class C[+A] covariant
class C[-A] contravariant
class C[A] nonavariant
 */
type A = IntSet => NonEmpty
type B = NonEmpty => IntSet
//  A <: B
//  내가 이해하기로는
//  A(NonEmpty, IntSet)으로 호출하는 게 가능하지만 B(NonEmpty)만 가능하기 때문에
//  A는 B의 subtype이므로 A <: B
//  NonEmpty <: IntSet, 즉 NonEmpty는 IntSet의 subtype이기 때문에
//  A는 IntSet의 subtype인 NonEmtpy로 호출 가능
//  반대로 출력의 경우 NonEmpty는 IntSet의 subtype, 즉 special case이기 때문에
//  A가 B의 subtype이고 A는 B + more
//  ban diagram으로 그려보면 이해가 조금 쉬움

/*
generally, if A2 <: A1 and B1 <: B2, then
A1 => B1 <: A2 => B2
 */