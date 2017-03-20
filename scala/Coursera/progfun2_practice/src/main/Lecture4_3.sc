import scala.util.DynamicVariable
//  Lecture 4-3
/*
class Signal[T](expr: => T) {
  def apply(): T = ???
}
object Signal {
  def apply[T](expr: => T) = new Signal(expr)
}
class Var[T](expr: => T) extends Signal[T](expr)  {
  def update(expr: => T): Unit = ???
}
object Var  {
  def apply[T](expr: => T) = new Var(expr)
}
*/

//  Each signal maintains
//    its current value
//    the current expression that defines the signal value
//    a set of observers; the other signals that depend on its value

class Signal[T](expr: => T) {
  import Signal._
  private var myExpr: () => T = _
  private var myValue: T = _
  private var observers: Set[Signal[_]] = Set()
  update(expr)

  protected def update(expr: => T): Unit = {
    myExpr = () => expr
    computeValue()
  }

  protected def computeValue(): Unit = {
    val newValue = caller.withValue(this)(myExpr())
    if ( myValue != newValue )  {
      myValue = newValue
      val obs = observers
      observers = Set()
      obs.foreach(_.computeValue())
    }
  }

  def apply() = {
    observers += caller.value
    assert(!caller.value.observers.contains(this), "cyclic signal definition")
    myValue
  }
}

object Signal {
  private val caller = new DynamicVariable[Signal[_]](NoSignal)
  def apply[T](expr: => T) = new Signal(expr)
}

object NoSignal extends Signal[Nothing](???)  {
  override def computeValue() = ()
}

class Var[T](expr: => T) extends Signal[T](expr)  {
  override def update(expr: => T): Unit = super.update(expr)
}

object Var  {
  def apply[T](expr: => T) = new Var(expr)
}