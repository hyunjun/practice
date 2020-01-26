import akka.actor.{ActorSystem, Props}

object ActorsHierarchy extends App {
  // 액터 시스템 생성 . 이름은 mysystem
  val ourSystem = ActorSystem("mysystem")

  val parent = ourSystem.actorOf(Props[ParentActor], "parent")
  parent ! "create"
  parent ! "create"
  Thread.sleep(1000)
  parent ! "hi"
  Thread.sleep(1000)
  parent ! "stop"
  Thread.sleep(1000)
  ourSystem.terminate()
}
