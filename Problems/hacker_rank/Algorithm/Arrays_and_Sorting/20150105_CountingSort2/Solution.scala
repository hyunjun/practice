object Solution {
  def countingSort(ar: Array[Int]): Array[Int] = {
    val counts: Array[Int] = Array.fill[Int](100)(0)
    for ( a <- ar ) {
      counts(a) += 1
    }
    var idx: Int = 0
    var res: Array[Int] = Array()
    for ( (c, i) <- counts.zipWithIndex ) {
      if ( 0 < c )  {
        res = res ++ Array.fill[Int](c)(i)
      }
    }
    res
  }

  def main(args: Array[String]) {
    val inps = io.Source.stdin.getLines.drop(1).toArray
    val ar = inps(0).split(" ").map((s: String) => s.toInt).toArray
    val res = countingSort(ar)
    println(res.mkString(" "))
  }
}
