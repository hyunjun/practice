// Functional decomposition using pattern matching
trait Expr
case class Number(n: Int) extends Expr
case class Sum(e1: Expr, e2: Expr) extends Expr

//  companion objects with apply methods
object Number {
  def apply(n: Int): Number = new Number(n)
}

object Sum  {
  def apply(e1: Expr, e2: Expr): Sum = new Sum(e1, e2)
}

Number(1)

def eval(e: Expr): Int = e match {
  case Number(n) => n
  case Sum(e1, e2) => eval(e1) + eval(e2)
}

eval(Sum(Number(1), Number(2)))

/*  //  possible, too
trait Expr  {
  def eval(e: Expr): Int = e match {
    case Number(n) => n
    case Sum(e1, e2) => eval(e1) + eval(e2)
  }
}
 */

def show(e: Expr): String = e match {
  case Number(n) => n.toString
  case Sum(e1, e2) => show(e1) + " + " + show(e2)
}

show(Sum(Number(1), Number(2)))

//  Sum(Prod(2, Var("x")), Var("y")) should print "2 * x + y"
//  Prod(Sum(2, Var("x")), Var("y")) should print "(2 + x) * y"