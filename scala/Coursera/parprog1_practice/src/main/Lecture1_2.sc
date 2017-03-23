class HelloThread extends Thread  {
  override def run(): Unit =  {
    println("Hello World!")
  }
}
val t = new HelloThread
t.start()
t.join()

class HelloThread2 extends Thread {
  override def run() = {
    println("hello")
    println("world")
  }
}

val t2 = new HelloThread2
val s = new HelloThread2
t2.start()
s.start()
t2.join()
s.join()

private var uidCount = 0L
def getUniqueId(): Long = {
  uidCount = uidCount + 1
  uidCount
}

def startThread() = {
  val t = new Thread  {
    override def run(): Unit =  {
      val uids = for ( i <- 0 until 10 ) yield getUniqueId()
      println(uids)
    }
  }
  t.start()
  t
}

/*
scala> startThread(); startThread()
Vector(1, 3, 5, 6, 7, 8, 9, 10, 12, 13)
Vector(1, 2, 4, 5, 6, 7, 8, 9, 10, 11)
res0: Thread = Thread[Thread-3,5,]
 */

/*private*/ val x = new AnyRef {}
private var uidCount2 = 0L
def getUniqueId2(): Long = x.synchronized {
  uidCount2 = uidCount2 + 1
  uidCount2
}

//  Lecture 1-3
//  Composition of the synchronized block can nest
class Account(private var amount: Int = 0)  {
  def transfer(target: Account, n: Int) =
    this.synchronized {
      target.synchronized {
        this.amount -= n
        target.amount += n
      }
    }
}

def startThread2(a: Account, b: Account, n: Int) = {
  val t = new Thread{
    override def run(): Unit =  {
      for ( i <- 0 until n )  {
        a.transfer(b, 1)
      }
    }
  }
  t.start()
  t
}
val a1 = new Account(500000)
val a2 = new Account(700000)
val t3 = startThread2(a1, a2, 150000)
val s3 = startThread2(a2, a1, 150000)
t3.join()
s3.join()
//  never complete > Deadlock
//  wait for each to finish without releasing the already acquired resources
/*
val a = new Account(50)
val b = new Account(70)
a.transfer(b, 10)
b.transfer(a, 10)
 */

//  One approach is to always acquire resources in the same order
//  This assumes an ordering relationship on the resources
class Account2(private var amount: Int = 0)  {
  val uid = getUniqueId()
  private def lockAndTransfer(target: Account2, n: Int) =
    this.synchronized {
      target.synchronized {
        this.amount -= n
        target.amount += n
      }
    }
  def transfer(target: Account2, n: Int) =
    if ( this.uid < target.uid ) this.lockAndTransfer(target, n)
    else target.lockAndTransfer(this, -n)
}

//  Memory model
//  a set of rules that describes how threads interact when accessing shared memory
//  1. Two threads writing to separate locations in memory
//     do not need synchronization
//  2. A thread X that calls join on another thread Y is guaranteed
//     to observer all the writes by thread Y after join returns
