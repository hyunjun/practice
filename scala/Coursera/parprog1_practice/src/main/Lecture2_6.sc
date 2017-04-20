//  Parallel Scan(Prefix Sum) Operation

List(1, 3, 8).scanLeft(100)((s, x) => s + x)
//List(a1, a2, a3).scanLeft(a0)(f) = List(b0, b1, b2, b3)
//b0 = a0
//b1 = f(b0, a1)
//b2 = f(b1, a2)
//b3 = f(b2, a3)

List(1, 3, 8).scanRight(100)(_ + _)

def scanLeft[A](inp: Array[A], a0: A, f: (A, A) => A, out: Array[A]): Unit = {
  out(0) = a0
  var a = a0
  var i = 0
  while ( i < inp.length ) {
    a = f(a, inp(i))
    i = i + 1
    out(i) = a
  }
}

//  making scan parallel, O(logN)
/*
def reduceSeg1[A](inp: Array[A], left: Int, right: Int, a0: A, f: (A, A) => A): A
def mapSeg[A, B](inp: Array[A], left: Int, right: Int, fi: (Int, A) => B, out: Array[B]): Unit

def scanLeft2[A](inp: Array[A], a0: A, f: (A, A) => A, out: Array[A]) = {
  val fi = { (i: Int, v: A) => reduceSeg1(inp, 0, i, a0, f) }
  mapSeg(inp, 0, inp.length, fi, out)
  val last = inp.length - 1
  out(last + 1) = f(out(last), inp(last))
}
*/

//  Tree definitions
//  Trees storing our input collection only have values in leaves
sealed abstract class Tree[A]
case class Leaf[A](a: A) extends Tree[A]
case class Node[A](l: Tree[A], r: Tree[A]) extends Tree[A]
//  Trees storing intermediate values also have (res) values in nodes
sealed abstract class TreeRes[A] { val res: A }
case class LeafRes[A](override val res: A) extends TreeRes[A]
case class NodeRes[A](l: TreeRes[A], override val res: A, r: TreeRes[A]) extends TreeRes[A]

def reduceRes[A](t: Tree[A], f: (A, A) => A): TreeRes[A] = t match {
  case Leaf(v) => LeafRes(v)
  case Node(l, r) => {
    val (tL, tR) = (reduceRes(l, f), reduceRes(r, f))
    NodeRes(tL, f(tL.res, tR.res), tR)
  }
}
val t1 = Node(Node(Leaf(1), Leaf(3)), Node(Leaf(8), Leaf(50)))
val plus = (x: Int, y: Int) => x + y
reduceRes(t1, plus)

/*
def upsweep[A](t: Tree[A], f: (A, A) => A): TreeRes[A] = t match {
  case Leaf(v) => LeafRes(v)
  case Node(l, r) =>
    val (tL, tR) = parallel(upsweep(l, f), upsweep(r, f))
    NodeRes(tL, f(tL.res, tR.res), tR)
}
def downsweep[A](t: TreeRes[A], a0: A, f: (A, A) => A): Tree[A] = t match {
  case LeafRes(a) => Leaf(f(a0, a))
  case NodeRes(l, _, r) => {
    val (tL, tR) = parallel(downsweep(l, a0, f),
                            downsweep(r, f(a0, l.res), f))
    Node(tL, tR)
  }
}
def scanLeft[A](t: Tree[A], a0: A, f: (A, A) => A): Tree[A] = {
  val tRes = upsweep(t, f)
  val scan1 = downsweep(tRes, a0, f)
  prepend(a0, scan1)
}
//  without regarding skewness
def prepend[A](x: A, t: Tree[A]): Tree[A] = t match {
  case Leaf(v) => Node(Leaf(x), Leaf(v))
  case Node(l, r) => Node(prepend(x, l), r)
}
*/
