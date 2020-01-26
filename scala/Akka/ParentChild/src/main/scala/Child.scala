import akka.actor.Actor
import akka.event.Logging

class ChildActor extends Actor {
  val log = Logging(context.system, this)
  def receive = {
    case "hi" =>
      val parent = context.parent
      log.info(s"my parent $parent made me say hi!")
  }
  override def postStop() {
    log.info("child stopped!")
  }
}
