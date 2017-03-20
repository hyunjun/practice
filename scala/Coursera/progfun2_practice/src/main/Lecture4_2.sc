//  Lecture 4-2
//  Functional Reactive Programming
//  Functional view: Aggregate an event sequence into a signal
//    A signal is a value that changes over time
//    It is represented as a function from time to the value domain
//    Instead of propagating updates to mutable state, we define new signals in terms of existing ones

//  Example: Mouse Positions
//  Event-based view: Whenever the mouse moves, an event
//    MouseMoved(toPos: Position)
//  is Fired
//  FRP view:
//  A signal,
//    mousePosition: Signal[Position]
//  which at any point in time represents the current mouse position

//  Rx are related but the term FRP is not commonly used for them

//  Fundamental Signal Operations
//  mousePosition() //  the current mous position
/*  def inReactangle(LL: Position, UR: Position): Signal[Boolean] =
      Signal {
        val pos = mousePosition()
        LL <= pos && pos <= UR
      }
 */
//  val sig = Signal(3) //  always 3
/*  val sig = Var(3)
    sig.update(5) //  From now on, sig returns 5 instead of 3
    sig() = 5     //  abbreviation
    //  array arr
    arr(i) = 0  //  translated to arr.update(i, 0)
*/

//  map over signals, which gives us a relation between two signals that is maintained automatically, at all future points in time
//  No such mechanism exists for mutable variables
/*
a = 2
b = 2 * a
a = a + 1
b = 2 * a

a() = 2
b() = 2 * a()
a() = 3
//  b automatically updated
 */

class BankAccount {
  val balance = Var(0)
  def deposit(amount: Int): Unit =
    if ( amount > 0 ) {
      val b = balance()
      balance() = b + amount
    }
  def withdraw(amount: Int): Unit =
    if ( 0 < amount && amount <= balance() )  {
      val b = balance()
      balance() = b - amount
    } else throw new Error("insufficient funds")
}

object accounts {
  def consolidated(accts: List[BankAccount]): Signal[Int] =
    Signal(accts.map(_.balance()).sum)

  val a = new BankAccount()
  val b = new BankAccount()
  val c = consolidated(List(a, b))
  c()
  a deposit 20
  c()
  b deposit 30
  c()
  val xchange = Signal(246.00)
  val inDollar = Signal(c() * xchange())
  inDollar()
  b withdraw 10
  inDollar()
}
