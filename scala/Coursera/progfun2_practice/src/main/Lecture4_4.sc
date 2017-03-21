//  Lecture 4-4

//  The Four Essential Effects in Programming
/*
              One       Many
Synchronous   T/Try[T]  Iterable[T]
Asynchronous  Future[T] Observable[T]
 */

trait Adventure {
  def collectCoins(): List[Coin]
  //  def readFromMemory(): Array[Byte]
  def buyTreasure(coins: List[Coin]): Treasure
  //  sendToEurope(packet: Array[Byte]): Array[Byte]
}

val adventure = Adventure()
//  val socket = Socket()
val coins = adventure.collectCoins()
//  val packet = socket.readFromMemory()  //  only continues if no exception
val treasure = adventure.buyTreasure(coins)
//  val confirmation = socket.sendToEurope(packet)  //  only continues if no exception

//  Isn't there any Monads for that?

//  Lecture 4-5
//  Future[T]
//  A monad that handles exceptions and latency

//  Futures asynchronously notify consumers
import scala.concurrent._
import scala.concurrent.ExecutionContext.Implicits.global

trait Future[T] {
  //def onComplete(callback: Try[T] => Unit)
  //  (implicit executor: ExecutionContext): Unit
  def onComplete(success: T => Unit, failed: Throwable => Unit): Unit
  def onComplete(callback: Observer[T]): Unit
}

//  callback needs to use pattern matching
/*
ts match  {
  case Success(t) => onNext(t)
  case Failure(e) => onError(e)
}
*/
trait Observer[T] {
  def onNext(value: T): Unit
  def onError(error: Throwable): Unit
}
//  ???
//  An object is a closure with multiple methods
//  A closure is an object with a single method

trait Socket  {
  def readFromMemory(): Future[Array[Byte]]
  def sendToEurope(packet: Array[Byte]): Future[Array[Byte]]
}
val socket = Socket()
val packet: Future[Array[Byte]] = socket.readFromMemory()
packate.onComplete  {
  case Success(p) => {
    val confirmation: Future[Array[Byte]] = socket.sendToEurope(p)
  }
  case Failure(t) =>   ...
}
