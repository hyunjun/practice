import akka.actor.{ ActorRef, ActorSystem, Props, Actor }
import akka.event.Logging


// 나의 액터 클래스
class Hello(val hello: String) extends Actor {
  val log = Logging(context.system, this)

  def receive = {
    case `hello` => // 받은 메세지가 'hello' 라면
      log.info(s"Received a $hello!")
    case msg   =>  // 받은 메세지가 아무것이라면
      log.info(s"Unexpected message '$msg'")
      context.stop(self)
  }
}


object ActorsCreate extends App {

  // 액터 시스템 생성 . 이름은 mysystem
  val mySystem = ActorSystem("mysystem")

  // 액터 시스템을 통하여 나의 Actor 생성. 이름은 greeter 타입은 ActorRef
  val hiActor : ActorRef = mySystem.actorOf(Props(new Hello("hi")), name = "greeter")

  // 나의 액터와 교신. 'hi' 라는 메세지를 보낸다. // Received a hi! 출력
  hiActor ! "hi"
  Thread.sleep(1000)

  // 나의 액터와 교신. 3 이라는 메세지를 보낸다. // Unexpected message '3' 출력
  hiActor ! 3
  Thread.sleep(1000)

  // 액터 시스템 종료
  mySystem.terminate()
}

