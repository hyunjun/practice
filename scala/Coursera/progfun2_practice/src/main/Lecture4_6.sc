//  Lecture 4-6

/*
val socket = Socket()
val packet: Future[Array[Byte]] =
  socket.readFromMemory()
val confirmation: Future[Array[Byte]] =
  packet.flatMap(p => socket.sendToEurope(p))
*/

//  Lecture 4-7
/*
def fallbackTo(that: => Future[T]): Future[T] = {
  this recoverWith  {
    case _ => that recoverWith { case _ => this }
  }
}
*/
/*
val socket = Socket()
val packet: Future[Array[Byte]] =
  socket.readFromMemory()
val confirmation: Future[Array[Byte]] =
  packet.flatMap(socket.sendToSafe(_))

val c = Await.result(confirmation, 2 seconds)
println(c.toText)
*/