//  https://www.coursera.org/learn/parprog1/lecture/FdEvs/splitters-and-combiners

//  Iterator
/*
trait Iterator[A] {
  def next(): A //  can be called only if hasNext returns true
  def hasNext: Boolean
}

def iterator: Iterator[A] //  on every collection

//  implement foldLeft on an interator
def foldLeft[B](z: B)(f: (B, A) => B): B = {
  var result = z
  while ( hasNext ) s = f(s, next())
  s
}
*/

//  Splitter
/*
trait Splitter[A] extends Iterator[A] {
  def split: Seq[Splitter[A]]
    //  after calling split, the original splitter is left in an undefined state
    //  the resulting splitters traverse disjoint subsets of the original splitter
    //  reamining is an estimate on the number of remaining elements
    //  split is an efficient method - O(logN) or better
  def remaining: Int
}
def splitter: Splitter[A] //  on every parallel collection

//  implement fold on a splitter
def fold(z: T)(f: (T, T) => T): T = {
  if ( remaining < threshold ) foldLeft(z)(f)
  else  {
    val children: Seq[Task[T]] = for ( child <- split ) yield task { child.fold(z)(f) }
    children.map(_.join()).foldLeft(z)(f)
  }
}
*/

//  Builder
/*
trait Builder[A, Repr]  {
  def += (elem: A): Builder[A, Repr]
  def result: Repr
  //  calling result returns a collection of type Repr, containing the elements
  //    that were previously added with +=
  //  calling result leaves the Builder in an undefined state
}
def newBuilder: Builder[A, Repr]  //  on every collection

def filter(p: T => Boolean): Traversable[T] = {
  val b = newBuilder
  for ( x <- this ) if (p(x)) b += x
  b.result
}
*/

//  Combiner
/*
trait Combiner[A, Repr] extends Builder[A, Repr]  {
  def combine(that: Combiner[A, Repr]): Combiner[A, Repr]
  //  calling combine returns a new combiner that contains elements of input combiners
  //  calling combine leaves both original Combiners in an undefined state
  //  combine is an efficient method - O(logN) or better
}
def newCombiner: Combiner[T, Repr]  //  on every parallel collection
*/
