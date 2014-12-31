object Solution {
  def quickSort(ar: Array[Int]): Array[Int] = {
    var left = ar.filter(_ < ar(0))
    if ( 1 < left.length )  {
      left = quickSort(left)
      println(left.mkString(" "))
    }
    var right = ar.filter(ar(0) < _)
    if ( 1 < right.length ) {
      right = quickSort(right)
      println(right.mkString(" "))
    }
    (left :+ ar(0)) ++ right
  }

  def main(args: Array[String]) {
    val inps = io.Source.stdin.getLines.drop(1).toArray
    val ar = inps(0).split(" ").map((s: String) => s.toInt).toArray
    val res = quickSort(ar)
    println(res.mkString(" "))
  }
}
