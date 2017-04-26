//  https://www.coursera.org/learn/parprog1/lecture/vOFRq/data-parallel-programming

//  Data-Parallel Programming Model
def initializeArray(xs: Array[Int])(v: Int): Unit = {
  for ( i <- (0 until xs.length).par ) {
    xs(i) = v
  }
}
//  The parallel for loop is not functional

//  Mandelbrot Set
//  Zn+1 = Zn^2 + c
//  c > c^2 + c > (c^2 + c)^2 + c > ... > |Zi| >= 2 > ... |Zmax| < 2
/*
private def computePixel(xc: Double, yc: Double, maxIterations: Int): Int = {
  var i = 0
  var x, y = 0.0
  while (x * x + y * y < 4 && i < maxIterations) {
    val xt = x * x - y * y + xc
    val yt = 2 * x * y + yc
    x = xt
    y = yt
    i += 1
  }
  color(i)
}

def parRender(): Unit = {
  for ( idx <- (0 until image.length).par ) {
    val (xc, yc) = coordinatesFor(idx)
    image(idx) = computePixel(xc, yc, maxIterations = )
  }
}
*/
//  data-parallel implementation 2 times faster than task-parallel implementation

//  https://www.coursera.org/learn/parprog1/lecture/efzVT/data-parallel-operations-i
(1 until 1000).par
  .filter(n => n % 3 == 0)
  .count(n => n.toString == n.toString.reverse)
//  Non-Parallelizable operations
def sum(xs: Array[Int]): Int = {
  xs.par.foldLeft(0)(_ + _) //  is parallel?
}
//  def foldLeft[B](z: B)(f: (B, A) => B): B
//  (B, A) => B   이 부분을 lego로 설명
//  foldRight, reduceLeft, reduceRight, scanLeft, scanRight 다 마찬가지

//  def fold(z: A)(f: (A, A) => A): A
//  (A, A) => A   이 부분을 lego로 설명  simlilar to reduction tree
//  execute in parallel possible

//  https://www.coursera.org/learn/parprog1/lecture/shwKn/data-parallel-operations-ii
def sum2(xs: Array[Int]): Int = {
  xs.par.fold(0)(_ + _)
}
def max(xs: Array[Int]): Int = {
  xs.par.fold(Int.MinValue)(math.max)
                           //(x, y) => if ( x >y ) x else y
}
//  f(x, z) = f(z, x) = x
//  0 + 117 = 117
//  f(x1, f(x2, x3)) = f(f(x1, x2), x3)

Array("paper", "rock", "paper", "scissors") //  who won?

def play(a: String, b: String): String = List(a, b).sorted match {
  case List("paper", "scissors") => "scissors"
  case List("paper", "rock") => "paper"
  case List("rock", "scissors") => "rock"
  case List(a, b) if a == b => a
  case List("", b) => b
}
Array("paper", "rock", "paper", "scissors")
  .par.fold("")(play)
play(play("paper", "rock"), play("paper", "scissors"))
play("paper", play("rock", play("paper", "scissors")))  //  wrong, not associative
//  associative f(a, f(b, c)) == f(f(a, b), c)
//  commutative f(z, a) == f(a, z) == a
//  the neutral element z and the binary operator f must form a monoid
//  Commutativity does not matter for fold

def isVowel(c: String): Boolean = c.toLowerCase match {
  case "a" => true
  case "e" => true
  case "i" => true
  case "o" => true
  case "u" => true
  case _ => false
}
Array("E", "P", "F", "L")
//  .par.fold(0)((count, c) => if (isVowel(c)) count + 1 else count)
//  fold should have the same type as the collection
//  def fold(z: A)(op: (A, A) => A): A = foldLeft[A](z)(op)

//  def aggregate[B](z: B)(f: (B, A) => B, g: (B, B) => B): B
//  역시 lego 그림으로 설명...
Array("E", "P", "F", "L")
  .par.aggregate(0)(
  (count, c) => if (isVowel(c)) count + 1 else count,
  _ + _ //  0 and this line are monoid
)

//  so far, we saw the accessor combinators
//  Transformer combinators, such as map, filter, flatMap and groupBy
//    do not return a single value, but instead return new collections as results
