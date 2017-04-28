//  https://www.coursera.org/learn/parprog1/lecture/dB4xX/implementing-combiners

/*
trait Builder[T, Repr]  {
  def += (elem: T): this.type
  def result: Repr
}

e.g.
T = String
Repr = Seq[String]
"Adam", "Bob", "Eve"
Builder[String, Seq[String]]
  += "Adam"
  += "Bob"
  += "Eve"
 */

/*
trait Combiner[T, Repr] extends Builder[T, Repr]  {
  def combine(that: Combiner[T, Rerp]): Combiner[T, Repr]
}

this; x, y, z
that: u, v, w
combine; x, y, z, u, v, w

//  How can we implement combiner efficiently?
//  Repr; set or map > combine = union
//  Repr; sequence > combine = concatenation
//  combine must be efficient, i.e. execute in O(logN + logM)
//    N, M are the sizes of two input combiners
 */

def combine(xs: Array[Int], ys: Array[Int]): Array[Int] = {
  val r = new Array[Int](xs.length + ys.length)
  Array.copy(xs, 0, r, 0, xs.length)
  Array.copy(ys, 0, r, xs.length, ys.length)
  r
}
//  is it efficient enough? NO, because O(N + M)

//  Problem; always cannot be efficiently concatenated
//  hash tables O(1)
//  balanced trees O(logN)
//  linked list O(N)

//  mutable linked lists O(1) prepend and append, O(N) insertion
//  functional (cons) lists O(1) prepend, O(N) else
//  array lists - amortized O(1) append, O(1) random accesses, O(N) else
