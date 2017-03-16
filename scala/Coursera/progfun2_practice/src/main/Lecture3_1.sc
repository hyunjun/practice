//  Lecture 3-1
//  Reminder; Substitution Model

//  Stateful Object
var x: String = "abc"
var count = 111
x = "hi"
count = count + 1

class BankAccount {
  private var balance = 0 //  state
  def deposit(amount: Int): Unit = {
    if ( amount > 0 ) balance = balance + amount
  }
  def withdraw(amount: Int): Int =
    if ( 0 < amount && amount <= balance )  {
      balance = balance - amount
      balance
    } else
      throw new Error("insufficient funds")
}
val account = new BankAccount
account deposit 50
account withdraw 20
account withdraw 20
//account withdraw 15

/*def cons[T](hd: T, tl: => Stream[T]) = new Stream[T]  {
  def head = hd
  private var tlOpt: Option[Stream[T]] = None
  def tail: T = tlOpt match {
    case Some(x) => x
    case None => tlOpt = Some(tl); tail
  }
}*/

//  Stateful? yes because its history affects
class BankAccountProxy(ba: BankAccount) {
  def deposit(amount: Int): Unit = ba.deposit(amount)
  def withdraw(amount: Int): Int = ba.withdraw(amount)
}

//  Lecture 3-2 Identity and Change

//  referential transparency
//  val x = E; val y = E
//  val x = E; val y = x

//  operational equivalence
//  x and y are operationally equivalent if no possible test can distinguish between them
val xb = new BankAccount
val yb = new BankAccount
//  f(xb, xb) vs. f(xb, yb); same result or not
// test1
//xb deposit 30
//yb withdraw 20
// test2
//xb deposit 30
//xb withdraw 20
val xc = new BankAccount
val yc = xc
//  val xc = new BankAccount
//  val yc = new BankAccount  //  substitution model
//  It is possible to adapt the substitution model by introducing a store, but complicated

//  Lecture 3-3 Loops
def power(x: Double, exp: Int): Double = {
  var r = 1.0
  var i = exp
  while ( i > 0 ) { r = r * x; i = i - 1 }  //  while is a keyword
  r
}
//  define while using a function
def WHILE(condition: => Boolean)(command: => Unit): Unit =
  if ( condition )  {
    command
    WHILE(condition)(command) //  tail recursive
  }
  else  ()

/*
  REPEAT {
    command
  } ( condition )
 */
def REPEAT(command: => Unit)(condition: => Boolean): Unit = {
  command
  if ( condition )  ()
  else  REPEAT(command)(condition)
}

/*
  REPEAT  {
    command
  } UNTIL ( condition )
 */
//  for ( int i = 1; i < 3; i = i + 1 ) { System.out.print(i + " "); }
for ( i <- 1 until 3 ) { System.out.print(i + " ") }
//  def foreach(f: T => Unit): Unit = ...
for ( i <- 1 until 3; j <- "abc" ) println(i + " " + j)
(1 until 3) foreach (i => "abc" foreach (j => println(i + " " + j)))