//  Lecture 2-3 Lazy Evaluation
//  by-name evaluation, strict evaluation

//lazy val x = expr
def expr = {
  val x = { print("x"); 1 }
  lazy val y = { print("y"); 2 }
  def z = { print("z"); 3 }
  z + y + x + z + y + x
}
expr

/*
def cons[T](hd: T, tl: => Stream[T]) = new Stream[T] {
  def head = hd
  lazy val tail = tl
}
*/