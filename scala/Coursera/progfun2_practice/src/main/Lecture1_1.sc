/*
val f: String => String = { case "ping" => "pong" }
f("ping")
//f("abc")
 */
val f: PartialFunction[String, String] = { case "ping" => "pong" }
f.isDefinedAt("ping")
f.isDefinedAt("pong")
f("ping")

//  Lecture 1-2
//  ::  Cons
//  ++  Concatenation
val N = 3
for {
  x <- 2 to N
  y <- 2 to x
  if ( x % y == 0 )
} yield(x, y)
(2 to N) flatMap(x =>
  (2 to x) withFilter (y =>
    x % y == 0) map (y => (x, y)))


//  Lecture 1-1
case class Book(title: String, authors: List[String])
val books: List[Book] = List(
  Book(title = "SICP",
    authors = List("A, H", "S, G J")),
  Book(title = "IFP",
    authors = List("B, R", "W, P"))
)
for ( b <- books; a <- b.authors if a startsWith "B" )
  yield b.title

//for ( b <- books if b.title indexOf "C" >= 0 )  //  NOT WORK, WHY?
for ( b <- books if b.title.indexOf("C") >= 0 )
  yield b.title

//  Lecture 1-2
books flatMap (b =>
  for ( a <- b.authors if a startsWith ("B" ) )
    yield b.title)
books flatMap (b =>
  for ( a <- b.authors withFilter(a => a.startsWith("B")) )
    yield b.title)
//  NOT WORK, WHY?
//books flatMap (b =>
//    b.authors withFilter(a => a startsWith "B")
//      map(y => y.title))

//  Lecture 1-3 random value generators
import java.util.Random
val rand = new Random
rand.nextInt

/*
trait Generator[+T] {
  def generate: T
}
val integers = new Generator[Int] {
  val rand = new java.util.Random
  def generate = rand.nextInt
}
val booleans = new Generator[Boolean] {
  def generate = integers.generate > 0
}
val pairs = new Generator[(Int, Int)] {
  def generate = (integers.generate, integers.generate)
}
val booleans2 = for ( x <- integers ) yield x > 0
//val booleans2 = integers map (x => x > 0) //  NOT WORK
def pairs2[T, U](t: Generator[T], u: Generator[U]) = for {
  x <- t
  y <- u
} yield (x, y)
*/
/*  //  NOT WORK
def pairs2[T, U](t: Generator[T], u: Generator[U]) =
  t flatMap (x => u map (y => (x, y)))
*/
trait Generator[+T] {
  self => //  an alias for "this"
  def generate: T
  def map[S](f: T => S): Generator[S] = new Generator[S]  {
    def generate = f(self.generate) //  to prevent infinite loop
  }
  def flatMap[S](f: T => Generator[S]): Generator[S] = new Generator[S] {
    def generate = f(self.generate).generate
  }
}
val integers = new Generator[Int] {
  val rand = new java.util.Random
  def generate = rand.nextInt
}
val booleans = integers map { x => x > 0 }
def pairs[T, U](t: Generator[T], u: Generator[U]) =
  t flatMap { x => u map { y => (x, y) }}
def single[T](x: T): Generator[T] = new Generator[T] {
  def generate = x
}
def choose(lo: Int, hi: Int): Generator[Int] =
  for ( x <- integers ) yield lo + x % (hi - lo)
def oneOf[T](xs: T*): Generator[T] =
  for ( idx <- choose(0, xs.length) ) yield xs(idx)
oneOf("red", "green", "yello")
def lists: Generator[List[Int]] = for {
  isEmpty <- booleans
  list <- if (isEmpty) emptyLists else nonEmptyLists
} yield list
def emptyLists = single(Nil)
def nonEmptyLists = for {
  head <- integers
  tail <- lists
} yield head :: tail

trait Tree
case class Inner(left: Tree, right: Tree) extends Tree
case class Leaf(x: Int) extends Tree
def leafs: Generator[Leaf] = for { x <- integers } yield Leaf(x)
def inners: Generator[Inner] = for {
  l <- trees
  r <- trees
} yield Inner(l, r)
def trees: Generator[Tree] = for {
  isLeaf <- booleans
  tree <- if ( isLeaf ) leafs else inners
} yield tree
trees.generate

//  Random Testing
def test[T](g: Generator[T], numTimes: Int = 100)
           (test: T => Boolean): Unit = {
  for ( i <- 0 until numTimes ) {
    val value = g.generate
    assert(test(value), "test failed for " + value)
  }
  println("passed " + numTimes + " times")
}
test(pairs(lists, lists)) {
  case (xs, ys) => (xs ++ ys).length >= xs.length
}

//  ScalaCheck, write properties
/*forAll { (l1: List[Int], l2: List[Int]) =>
  l1.size + l2.size == (l1 ++ l2).size
}*/