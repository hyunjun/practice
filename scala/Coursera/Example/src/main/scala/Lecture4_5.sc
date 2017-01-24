
trait Expr  {
  //  classification
  def isNumber: Boolean
  def isSum: Boolean
  //def isVar: Boolean
  //def isProd: Boolean
  //  accessor
  def numValue: Int
  def leftOp: Expr
  def rightOp: Expr
  //def name: String
}

class Number(n: Int) extends Expr {
  def isNumber: Boolean = true
  def isSum: Boolean = false
  def numValue: Int = n
  def leftOp: Expr = throw new Error("Number.leftOp")
  def rightOp: Expr = throw new Error("Number.rightOp")
}

class Sum(e1: Expr, e2: Expr) extends Expr  {
  def isNumber: Boolean = false
  def isSum: Boolean = true
  def numValue: Int = throw new Error("Sum.numValue")
  def leftOp: Expr = e1
  def rightOp: Expr = e2
}

def eval(e: Expr): Int = {
  if ( e.isNumber ) e.numValue
  else if ( e.isSum ) eval(e.leftOp) + eval(e.rightOp)
  else throw new Error("Unknown expression " + e)
}

eval(new Sum(new Number(1), new Number(2)))

//class Prod(e1: Expr, e2: Expr) extends Expr
//class Var(x: String) extends Expr

//  type test
//  x.isInstanceOf[T]
//  type case
//  x.asInstanceOf[T]
//  discouraged
def eval2(e: Expr): Int =
  if ( e.isInstanceOf[Number] )
    e.asInstanceOf[Number].numValue
  else if ( e.isInstanceOf[Sum] )
    eval(e.asInstanceOf[Sum].leftOp) + eval(e.asInstanceOf[Sum].rightOp)
  else
    throw new Error("Unknown expression " + e)
  //  + no need for classification methods
  //  + access methods only for classes where the value is defined
  //  - low-level and potentially unsafe


//  Solution1. Object-Oriented Decomposition
trait Expr1 {
  def eval: Int
}
class Number1(n: Int) extends Expr1 {
  def eval: Int = n
}
class Sum1(e1: Expr1, e2: Expr1) extends Expr1 {
  def eval: Int = e1.eval + e2.eval
}
//  There would be a problem if we add def show: String in trait Expr1
//  Limitations
//  a * b + a * c -> a * (b + c)  //  cannot be encapsulated in the method of a single object