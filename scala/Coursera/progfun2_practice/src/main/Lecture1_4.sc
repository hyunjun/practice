import scala.util.control.NonFatal
//  some algebraic laws, monads

//  monad = parametric type
trait M[T]  {
  def flatMap[U](f: T => M[U]): M[U]  //  more commonly called bind
}
def unit[T](x: T): M[T]

//  List is a monad with unit(x) = List(x)
//  Set, unit(x) = Set(x)
//  Option, unit(x) = Some(x)
//  Generator, unit(x) = single(x)
//  flatMap is an operation on each of these types, whereas unit in Scala is different for each monad

/*
//  map = combination of flatMap and unit
m map f == m flatMap (x => unit(f(x)))
        == m flatMap (f andThen unit)
*/

/*
//  Monad Laws -> Monoid, simpler form of Monad

//  Associativity
m flatMap f flatMap g == m flatMap (x => f(x) flatMap g)

//  Left unit
unit(x) flatMap f == f(x)

//  Right unit
m flatMap unit == m
 */

/*
//  Significance of the Laws for For-Expressions
for ( y <- for (x <- m; y <- f(x)) yield y
      z <- g(y) ) yield z
== for ( x <- m
         y <- f(x)
         z <- g(y) )
         yield z

//  Left unit X

for ( x <- m ) yield x == m
*/

//  type Try, to pass results of computations that can fail with an exception between threads and computers
abstract class Try[+T]
case class Success[T](x: T) extends Try[T]
case class Failure(ex: Exception) extends Try[Nothing]

/*
object Try  {
  def apply[T](expr: => T): Try[T] =
    try Success(expr)
    catch {
      case NonFatal(ex) => Failure(ex)
    }
}
//  Try(expr) //  gives Success(someValue) or Failure(someException)
*/

//  An expression composed from 'Try', 'map', 'flatMap' will never throw a non-fatal exception
//  Call this the "bullet-proof" principle

//  Many of the types defining flatMap are monads
//  also define withFilter, called "monads with zero"
