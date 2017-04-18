//  Parallel Fold (Reduce) Operation
List(1, 3, 8).foldLeft(100)((s, x) => s - x) == ((100 - 1) - 3) - 8
List(1, 3, 8).foldRight(100)((s, x) => s - x) == 1 - (3 - (8 - 100))
List(1, 3, 8).reduceLeft((s, x) => s - x) == (1 - 3) - 8
List(1, 3, 8).reduceRight((s, x) => s - x) == 1 - (3 - 8)

//  Associative operation
//  f(x, f(y, z)) = f(f(x, y), z)

sealed abstract class Tree[A]
case class Leaf[A](value: A) extends Tree[A]
case class Node[A](left: Tree[A], right: Tree[A]) extends Tree[A]

def reduce[A](t: Tree[A], f: (A, A) => A): A = t match {
  case Leaf(v) => v
  case Node(l, r) => f(reduce[A](l, f), reduce[A](r, f))
}

def tree = Node(Leaf(1), Node(Leaf(3), Leaf(8)))
def fMinus = (x: Int, y: Int) => x - y
def res = reduce[Int](tree, fMinus)

//  how to make that tree reduce parallel?
/*
def reduce[A](t: Tree[A], f: (A, A) => A): A = t match {
  case Leaf(v) => v
  case Node(l, r) => {
    val (lV, rV) = parallel(reduce[A](l, f), reduce[A](r, f))
    f(lV, rV)
  }
}
*/
//reduce(Node(Leaf(x), Node(Leaf(y), Leaf(z))), f) ==
//reduce(Node(Node(Leaf(x), Leaf(y)), Leaf(z)), f) ==

def toList[A](t: Tree[A]): List[A] = t match {
  case Leaf(v) => List(v)
  case Node(l, r) => toList[A](l) ++ toList[A](r)
}
def map[A, B](t: Tree[A], f: A => B): Tree[B] = t match {
  case Leaf(v) => Leaf(f(v))
  case Node(l, r) => Node(map[A, B](l, f), map[A, B](r, f))
}

//toList(t) == reduce(map(t, List(_)), _ ++ _)

//  if toList(t1) == toList(t2)
//  then, reduce(t1, f) == reduce(t2, f)

/*
def reduceSeg[A](inp: Array[A], left: Int, right: Int, f: (A, A) => A): A = {
  if ( right - left < threshold ) {
    var res = inp(left); var i = left + 1
    while ( i < right ) { res = f(res, inp(i)); i = i + 1 }
    res
  } else  {
    val mid = left + (right - left) / 2
    val (a1, a2) = parallel(reduceSeg(inp, left, mid, f),
                            reduceSeg(inp, mid, right, f))
    f(a1, a2)
  }
}
def reduce[A](inp: Array[A], f: (A, A) => A): A =
  reduceSeg(inp, 0, inp.length, f)
*/