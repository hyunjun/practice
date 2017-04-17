//  Data Operations and Parallel Mapping

//  operations on collections
List(1, 3, 8).map(x => x * x)
List(1, 3, 8).fold(100)((s, x) => s + x)
List(1, 3, 8).scan(100)((s, x) => s + x)

//  arrays; imperative(recall array sum)
//  trees; can be implemented functionally


/////////////////////////////////////////////////
//  Map
/////////////////////////////////////////////////
//  list.map(x => x) == list
//  list.map(f.compose(g)) == list.map(g).map(f)
//    (f.compose(g))(x) = f(g(x))

//  sequential definition
def mapSeq[A, B](lst: List[A], f: A => B): List[B] = lst match {
  case Nil => Nil
  case h :: t => f(h) :: mapSeq(t, f)
}

//  sequential map of an array producing an array
def mapASegSeq[A, B](inp: Array[A], left: Int, right: Int, f: A => B, out: Array[B]) = {
  var i = left
  while ( i < right ) {
    out(i) = f(inp(i))
    i = i + 1
  }
}
val in = Array(2, 3, 4, 5, 6)
val out = Array(0, 0, 0, 0, 0)
val f = (x: Int) => x * x
mapASegSeq(in, 1, 3, f, out)
out

//  parallel map of an array producing an array
//  writes need to be disjoint(otherwise non deterministic behavior)
//  threshold needs to be large enough
/*
def mapASegPar[A, B](inp: Array[A], left: Int, right: Int, f: A => B, out: Array[B]): Unit = {
  if ( right - left < threshold )
    mapASegSeq(inp, left, right, f, out)
  else  {
    val mid = left + (right - left) / 2
    parallel(mapASegPar(inp, left, mid, f, out),
             mapASegPar(inp, mid, right, f, out))
  }
}
*/

/*
//  sequential pointwise exponent written from scratch
def normsOf(inp: Array[Int], p: Double, left: Int, right: Int, out: Array[Double]): Unit = {
  var i = left
  while ( i < right ) {
    out(i) = power(inp(i), p)
    i = i + 1
  }
}
//  paralle pointwise exponent written from scratch
def normsOfPar(inp: Array[Int], p: Double, left: Int, right: Int, out: Array[Double]): Unit = {
  if ( right - left < threshold ) {
    var i = left
    while ( i < right ) {
      out(i) = power(inp(i), p)
      i = i + 1
    }
  } else  {
    val mid = left + (right - left) / 2
    parallel(normsOfPar(inp, p, left, mid, out),
             normsOfPar(inp, p, mid, right, out))
  }
}
*/


//  from lecturer's test
//  performance was about 7 times faster
//    when inp.length = 2000000, and threshold = 10000

//  parallel map on immutable trees
sealed abstract class Tree[A] { val size: Int }
case class Leaf[A](a: Array[A]) extends Tree[A] {
  override val size = a.size
}
case class Node[A](l: Tree[A], r: Tree[A]) extends Tree[A]  {
  override val size = l.size + r.size
}
/*
def mapTreePar[A:Manifest, B:Manifest](t: Tree[A], f: A => B): Tree[B] =
  t match {
    case Leaf(a) => {
      val len = a.length; val b = new Array[B](len)
      var i = 0
      while ( i < len ) { b(i) = f(a(i)); i = i + 1 }
      Leaf(b)
    }
    case Node(l, r) => {
      val (lb, rb) = parallel(mapTreePar(l, f), mapTreePar(r, f))
      Node(lb, rb)
    }
  }
*/

//  Comparison of arrays and immutable trees
//  Arrays
//  (+) random access to elements, on shared memory can share array
//  (+) good memory locality
//  (-) imperative: must ensure parallel tasks write to disjoint parts
//  (-) expensive to concatenate
//  Immutable trees
//  (+) purely functional, produce new trees, keep old ones
//  (+) no need to worry about disjointness of writes by paralle tasks
//  (+) efficient to combine two trees
//  (-) high memory allocation overhead
//  (-) bad locality