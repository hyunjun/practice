import scala.collection.mutable

//  Lecture 4-1 The Observer Pattern
//  publish / subscribe
//  model / view / controller (MVC)
trait Publisher {
  private var subscribers: Set[Subscriber] = Set()

  def subscribe(subscriber: Subscriber): Unit =
    subscribers += subscriber

  def unsubscribe(subscriber: Subscriber): Unit =
    subscribers -= subscriber

  def publish(): Unit
    subscribers.foreach(_.handler(this))
}

trait Subscriber  {
  def handler(pub: Publisher)
}

class BankAccount extends Publisher{
  private var balance = 0
  def currentBalance = balance

  def deposit(amount: Int): Unit =
    if ( amount > 0 ) {
      balance = balance + amount
      publish()
    }

  def withdraw(amount: Int): Unit =
    if ( 0 < amount && amount <= balance )  {
      balance = balance - amount
      publish()
    }
    else throw new Error("insufficient funds")
}

class Consolidator(observed: List[BankAccount]) extends Subscriber  {
  observed.foreach(_.subscribe(this))

  private var total: Int = _
  compute()

  private def compute() =
    total = observed.map(_.currentBalance).sum

  def handler(pub: Publisher) = compute()

  def totalBalance = total
}

val a = new BankAccount
val b = new BankAccount
val c = new Consolidator(List(a, b))
c.totalBalance
a deposit 20
c.totalBalance
b deposit 30
c.totalBalance

//  Good
//  Decoupes views from state
//  Allows to have a varying number of views of a given state
//  Simple to set up

//  Bad
//  Forces imperative style, since handlers are Unit-typed
//  Many moving parts that need to be co-ordinated
//  Concurrency makes things more complicated
//  Views are still tightly bound to one state; view update happens immediately

//  Adobe
//  1/3rd of the code in Adobe's desktop applications is devoted to event handling
//  1/2 of the bugs are found in this code