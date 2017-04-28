//  https://www.coursera.org/learn/parprog1/lecture/85Rfr/conc-tree-data-structure

/*
sealed trait List[+T] {
  def head: T
  def tail: List[T]
}
case class ::[T](head: T, tail: List[T]) extends List[T]

case object Nil extends List[Nothing] {
  def head = sys.error("empty list")
  def tail = sys.error("empty list")
}

def filter[T](lst: List[T])(p: T=>Boolean): List[T] = lst match {
  case x :: xs if p(x) => x :: filter(xs)(p)
  case x :: xs => filter(xs)(p)
  case Nil => Nil
}
*/

/*
sealed trait Tree[+T]
case class Node[T](left: Tree[T], right: Tree[T]) extends Tree[T]
case class Leaf[T](elem: T) extends Tree[T]
case object Empty extends Tree[Nothing]
*/

/*
def filter[T](t: Tree[T])(p: T => Boolean): Tree[T] = t match {
  case Node(left, right) => Node(parallel(filter(leaf)(p), filter(right)(p)))
  case Leaf(elem) => if (p(elem)) t else Empty
  case Empty => Empty
}
*/

//  Conc Data Type
//  conc-list data type introduced in the Fortress language
sealed trait Conc[+T] {
  def level: Int
  def size: Int
  def left: Conc[T]
  def right: Conc[T]
}
case object Empty extends Conc[Nothing]  {
  def level = 0
  def size = 0
}
class Single[T](val x: T) extends Conc[T]  {
  def level = 0
  def size = 1
}
//  <> node can never contain Empty as its subtree
//  level difference between the left and the right subtess of a <> node
//    is always 1 or less
case class <>[T](left: Conc[T], right: Conc[T]) extends Conc[T] {
  val level = 1 + math.max(left.level, right.level)
  val size = left.size + right.size
}

def <>(that: Conc[T]): Conc[T] = {
  if ( this == Empty ) that
  else if ( that == Empty ) this
  else concat(this, that)
}
def concat[T](xs: Conc[T], ys: Conc[T]): Conc[T] = {
  val diff = ys.level - xs.level
  if ( diff >= -1 && diff <= 1 ) new <>(xs, ys)
  else if ( diff < -1 ) {
    val nrr = concat(xs.right.right, ys)
    if ( nrr.level == xs.level - 3 )  {
      val nl = xs.left
      val nr = new <>(xs.right.left, nrr)
      new <>(nl, nr)
    } else  {
      val nl = new <>(xs.left, xs.right.left)
      val nr = nrr
      new <>(nl, nr)
    }
  }
}
//  <> method = O(h1 - h2)

//  Lecture 4-4
//  https://www.coursera.org/learn/parprog1/lecture/TH4HC/amortized-constant-time-append-operation

var xs: Conc[T] = Empty
def += (elem: T): Unit =  {
  xs = xs <> Single(elem)
}

case class Append[T](left: Conc[T], right: Conc[T]) extends Conc[T] {
  val level = 1 + math.max(left.level, right.level)
  val size = left.size + right.size
}
//def appendLeaf[T](xs: Conc[T], y: T): Conc[T] = Append(xs, new Single(y))
def appendLeaf[T](xs: Conc[T], ys: Single[T]): Conc[T] = xs match  {
  case Empty => sys
  case xs: Single[T] => new <>(xs, ys)
  case _ <> _ => new Append(xs, ys)
  case xs: Append[T] => append(xs, ys)
}
@tailrec private def append[T](xs: Append[T], ys: Conc[T]): Conc[T] = {
  if ( xs.right.level > ys.level ) new Append(xs, ys)
  else  {
    val zs = new <>(xs.right, ys)
    xs.left match {
      case ws @ Append(_, _) => append(ws, zs)
      case ws if ws.level <= zs.level => ws <> zs
      case ws => new Append(ws, zs)
    }
  }
}

//  Lecture 4-5
//  https://www.coursera.org/learn/parprog1/lecture/Gggrf/conc-tree-combiners

class ConcBuffer[T: ClassTag](val k: Int, private var conc: Conc[T])  {
  private var chunk: Array[T] = new Array(k)
  private var chunkSize: Int = 0
  final def += (elem: T): Unit = {
    if ( chunkSize >= k ) expand()
    chunk(chunkSize) = elem
    chunkSize += 1
  }

  private def expand(): Unit =  {
    conc = appendLeaf(conc, new Chunk(chunk, chunkSize))
    chunk = new Array(k)
    chunkSize = 0
  }

  final def combine(that: ConcBuffer[T]): ConcBuffer[T] = {
    val combinedConc = this.result <> that.result
    new ConcBuffer(k, combinedConc)
  }

  def result: Conc[T] = {
    conc = appendLeaf(conc, new Conc.Chunk(chunk, chunkSize))
    conc
  }
}
class Chunk[T](val array: Array[T], val size: Int) extends Conc[T]  {
  def level = 0
}
xs.par.aggregate(new ConcBuffer[String])(_ + _, _ combine _).result