//  Lecture 4-8
//  Composing Futures (1/2)

/*
val socket = Socket()
val confirmation: Future[Array[Byte]] = for {
  packet <- socket.readFromMemory()
  confirmation <- socket.sendToSafe(packet)
} yield confirmation

def retry(noTimes: Int)(block: => Future[T]): Future[T] = {
  ... retry successfully completing block at most noTimes
  ... and give up after that
}

//  Recursion is the GOTO of the functional programming
def retry(noTimes: Int)(block: =>Future[T]): Future[T] = {
  if ( noTimes == 0 ) {
    Future.failed(new Exception("Sorry"))
  } else  {
    block fallbackTo  {
      retry(noTimes - 1) { block }
    }
  }
}
*/

//  Lecture 4-9
//  Implementation of FlatMap
/*
trait Future[T] {
  def onComplete(callback: Try[T] => Unit) =   ...
  def flatMap[S](f: T => Future[S]): Future[S] = ???
}
*/
/*
trait Future[T] { self =>
  def flatMap[S](f: T => Future[S]): Future[S] =
    new Future[S] {
      def onComplete(callback: Try[S] => Unit): Unit =
        self onComplete {
          case Success(x) => f(x).onComplete(callback)
          case Failure(e) => callback(Failure(e))
        }
    }
}
*/

//  Lecture 4-10
//  Composing Futures (2/2)

//  folding lists
//  List(a, b, c).foldRight(e)(f)
//  f(a, f(b, f(c, e))) //  <-
//  List(a, b, c).foldLeft(e)(f)
//  f(f(f(e, a), b), c) //  ->
//  Like Northern wind comes from the North

/*
def retry(noTimes: Int)(block: => Future[T]): Future[T] = {
  val ns = (1 to noTimes).toList
  val attempts = ns.map(_ => ()=>block)
  val failed = Future.failed(new Exception("boom"))
  val result = attempts.foldLeft(failed)
  ((a, block) => a recoverWith { block() })
  result
}

retry(3) { block }
= unfolds to
((failed recoverWith {block1()})
    recoverWith {block2()})
      recoverWith {block3()}

ns = List(1, 2, ..., noTimes)
attempts = List(()=>block, ()=>block, ..., ()=>block)
                    block1     block2          block noTimes
result = (...((failed recoverWith {block1()})
                recoverWith {block2()}) ...)
                  recoverWith {block3()}
*/

/*
def retry(noTimes: Int)(block: =>Future[T]): Future[T] = {
  val ns = (1 to noTimes).toList
  val attempts: = ns.map(_ => () => block)
  val failed = Future.failed(new Exception)
  val result = attempts.foldRight(() =>failed)
  ((block, a)) => () => { block() fallbackTo { a() } })
  result ()
}

retry(3) { block } ()
= unfolds to
  block1 fallbackTo { block2 fallbackTo { block3 fallbackTo { failed }}}
*/

//  Conclustion
//  Functional Design Principles
//    lazy evaluation and infinite data structures
//    distinction between computations and values
//    monads to abstract over properties of computation
//      randomness, delays, effects
//    running computations at some later time

//  how to encapsulate mutations
//    laziness
//    FRP
//    monads