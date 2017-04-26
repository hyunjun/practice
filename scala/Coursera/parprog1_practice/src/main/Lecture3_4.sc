import scala.collection.{GenSeq, GenSet, mutable}
//  https://www.coursera.org/learn/parprog1/lecture/Udyw6/scala-parallel-collections
/*
Traversable[T]  e.g. foreach
Iterable[T]     e.g. iterator
Seq[T]
Set[T]
Map[K, V]
 */
/*
Traits
ParIterable[T], ParSeq[T], ParSet[T], ParMap[K, V]

generic traits
GenIterable[T], GenSeq[T], GenSet[T], GenMap[K, V]
 */
//  위의 3가지에 대한 상속 관계

def largestPalindrome(xs: GenSeq[Int]): Int = {
  xs.aggregate(Int.MinValue)(
    (largest, n) =>
    if (n > largest && n.toString == n.toString.reverse) n else largest,
    math.max
  )
}
val array = (0 until 1000000).toArray
largestPalindrome(array)

//  sequential collection can be converted into a parallel collection using par

/*
ParArray[T]
ParRange
ParVector[T]
immutable.ParHashSet[T]
immutable.ParHashMap[K, V]
mutable.ParHashSet[T]
mutable.ParHashMap[K, V]
ParTrieMap[K, V]
for other collections, par creates the closest parallel collection
  e.g. List is converted into ParVector
*/

def intersection(a: GenSet[Int], b: GenSet[Int]): Set[Int] = {
  val result = mutable.Set[Int]()
  for ( x <- a ) if ( b contains x ) result += x
  result.toSet
}
intersection((0 until 1000).toSet, (0 until 1000 by 4).toSet)
intersection((0 until 1000).par.toSet, (0 until 1000 by 4).par.toSet)
//  this program is NOT correct
//  problem is "result += x"

//  Rule
//  Avoid mutations to the same memory locations without proper synchronization
/*
//  compile error
import java.util.concurrent._
def intersection2(a: GenSet[Int], b: GenSet[Int]) = {
  val result = new ConcurrentSkipListSet[Int]()
  for ( x <- a ) if ( b contains a ) result += x
  result
}
intersection2((0 until 1000).toSet, (0 until 1000 by 4).toSet)
intersection2((0 until 1000).par.toSet, (0 until 1000 by 4).par.toSet)
*/

//  use filter as combinator
def intersection3(a: GenSet[Int], b: GenSet[Int]): GenSet[Int] = {
  if ( a.size < b.size ) a.filter(b(_)) //  Int => Boolean
  else b.filter(a(_))
}
intersection3((0 until 1000).toSet, (0 until 1000 by 4).toSet)
intersection3((0 until 1000).par.toSet, (0 until 1000 by 4).par.toSet)

//  Rule
//  Never modify a parallel collection
//    on which a data-parallel operation is in progress
/*
val graph = mutable.Map[Int, Int]() ++= (0 until 100000).map(i => (i, i + 1))
graph(graph.size - 1) = 0
for ((k, v) <- graph.par) graph(k) = graph(v)
val violation = graph.find({ case (i, v) => v != (i + 2) % graph.size })
println(s"violation: $violation")
*/

//  Never write to a collection that is conurrently traversed
//  Never read from a collection that is concurrently modified

/*
val graph = concurrent.TrieMap[Int, Int]()// ++= (0 until 100000).map(i => (i, i + 1))
graph(graph.size - 1) = 0
val previous = graph.snapshot()
for ((k, v) <- graph.par) graph(k) = previous(v)
val violation = graph.find({case (i, v) => v != (i + 2) % graph.size })
println(s"violation: $violation")
*/
