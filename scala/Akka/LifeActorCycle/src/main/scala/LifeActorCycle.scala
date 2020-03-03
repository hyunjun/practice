import akka.actor.{Actor, ActorRef, ActorSystem, Props}
import akka.event.Logging

class LifecycleActor extends Actor {
  val log = Logging(context.system, this)
  var child: ActorRef = _
  def receive = {
    case num: Double  => log.info(s"got a double - $num")
    case num: Int     => log.info(s"got an integer - $num")
    case lst: List[_] => log.info(s"list - ${lst.head}, ...")
    case txt: String  => child ! txt
  }
  override def preStart(): Unit = {
    log.info("preStart")
    child = context.actorOf(Props[StringPrinter], "kiddo")
  }
  override def preRestart(reason: Throwable, msg: Option[Any]): Unit = {
    log.info(s"preRestart because of $reason, during message $msg")
    super.preRestart(reason, msg)
  }
  override def postRestart(reason: Throwable): Unit = {
    log.info(s"postRestart due to $reason")
    super.postRestart(reason)
  }
  override def postStop() = log.info("postStop")
}


class StringPrinter extends Actor {
  val log = Logging(context.system, this)
  def receive = {
    case msg => log.info(s"child got message '$msg'")
  }
  override def preStart(): Unit = log.info(s"child preStart")
  override def postStop(): Unit = log.info(s"child postStop")
}


object ActorsLifecycle extends App {
  val ourSystem = ActorSystem("mysystem")
  val testy = ourSystem.actorOf(Props[LifecycleActor], "testy")
  testy ! math.Pi
  Thread.sleep(1000)
  testy ! 7
  Thread.sleep(1000)
  testy ! "hi there!"
  Thread.sleep(1000)
  testy ! List(1,2,3)

  Thread.sleep(1000)
  testy ! Nil
  Thread.sleep(1000)
  testy ! "sorry about that"
  Thread.sleep(1000)
  ourSystem.stop(testy)
  Thread.sleep(1000)
  ourSystem.terminate()
}
